from django.contrib.auth.forms import UserCreationForm


# 유저 ID 변경 안되게 하는 작업
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
