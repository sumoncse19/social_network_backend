For see the user from terminal:

```
python manage.py shell
```

```
from account.models import User
```

```
users = User.objects.all()
```

```
users
```

```
user = users.first()
```

```
user.email, user.name
```
