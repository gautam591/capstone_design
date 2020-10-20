from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisPosts.models import Post
from axisPMS.models import pmsPost

class uploadPostForm(forms.ModelForm):
    postTitle = forms.CharField(label='postTitle',required=True,
                                help_text='Title of this Post',
                                widget=forms.TextInput(attrs={'placeholder': 'Title/Heading','class':'newPostTitle'}))
    postAuthor = forms.CharField(label='postAuthor',required=False)
    content = forms.CharField(label='content',required=True,
                                help_text='Description of the Post',
                                widget=forms.Textarea(attrs={'placeholder': 'Write Your Post Here ...','class':'newPostContent'}))
    categoryChoices = [('0', 'select'),('1', 'south korea'),('2', 'japan'),('3', 'cananda'),('4', 'usa'),('5', 'australia')]
    country = forms.ChoiceField (label='category',required=False,
                                widget=forms.Select(attrs={'title': 'Post Category','class':'optionSelection'}),choices=categoryChoices)
    axisStatusChoices = [('0', 'None'),('1', 'Planning Phase'),('2', 'On Going'),('3', 'Suspended'),('4', 'Completed/Ended'),('5','Cancelled')]
    axisStatus = forms.ChoiceField (label='axisStatus',required=False,
                                widget=forms.Select(attrs={'title': 'Issue Status','class':'optionSelection'}),choices=axisStatusChoices)
    postLevelChoices = [('0', 'None'),('1', 'Government'),('2', 'Community'),('3', 'Private'),('4', 'Charity'),('5','Organization')]
    postLevel = forms.ChoiceField (label='axisStatus',required=False,
                                widget=forms.Select(attrs={'title': 'Issue Status','class':'optionSelection'}),choices=postLevelChoices)
    budget = forms.IntegerField(label='budget',required=False,initial=0,
                                widget=forms.NumberInput(attrs={'placeholder': 'Budget'}))
    startDate = forms.DateField(label='startDate',required=False,
                                widget=forms.SelectDateWidget(attrs={'class':'optionSelection'},empty_label=("Choose Year", "Choose Month", "Choose Day")))
    endDate = forms.DateField(label='endDate',required=False,
                                widget=AdminDateWidget)
    postImage = forms.ImageField(label="postImagae", required=False,help_text="Upload Images for Post")


    class Meta:
        model = Post
        fields = ["postTitle","content","postImage","country","axisStatus","postLevel","budget","startDate","endDate"]
