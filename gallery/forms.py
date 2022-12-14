from django import forms
from django.db.models import Count
from .models import IllustTag, IllustComment
from .widgets import CustomCheckboxSelectMultiple

class IllustSearchForm(forms.Form):
    """記事検索フォーム。"""
    key_word = forms.CharField(
        label = '検索キーワード',
        required = False,
    )

    tags = forms.ModelMultipleChoiceField(
        label = 'タグでの絞り込み',
        required = False,
        queryset=IllustTag.objects.annotate(illust_count=Count('illust')).order_by('name'),  # 変更
        widget = CustomCheckboxSelectMultiple
    )
    


class IllustCommentCreateForm(forms.ModelForm):
    class Meta:
        model = IllustComment
        exclude = ('target', 'created_at', "is_public")
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': "こちらにコメントをどうぞ"}
            )
        }