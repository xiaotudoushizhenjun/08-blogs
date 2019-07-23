# from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Category, Tag, Post


# 自定义编辑页面中表单元素的样式，调用自动补全接口
class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    # 使用自动补全的接口组件
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        # 参数url对应的是url中的name
        # widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    # tag为多对对字段，组件名跟category有差异
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        # 这边也不一样
        # widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )

    content_ck = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=False)
    content_md = forms.CharField(widget=forms.Textarea(), label='正文', required=False)
    content = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Post
        fields = (
            'category', 'tag', 'title', 'desc',
            'is_md', 'content', 'content_md', 'content_ck',
            'status'
        )

    def __init__(self, instance=None, initial=None, **kwargs):
        initial = initial or {}
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content

        super().__init__(instance=instance, initial=initial, **kwargs)

    def clean(self):
        is_md = self.cleaned_data.get('is_md')
        if is_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name, '必填项！')
            return
        self.cleaned_data['content'] = content
        return super().clean()

    class Media:
        js = ('js/post_editor.js', )
