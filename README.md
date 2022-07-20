# Platzi awards app
a poll app based on official Django documentation, it includes topics as:

- Models
- Views (function base views and class based views)
- Templates (with template inheritance based on jinja 2)
- Forms (forms.Form and form.ModelForm)
- Static Files
- Media files
- Django admin
- Django authentication
- Unit test

## Requirements and versions
- ***Django=3.2.9***

## Notes

- Remember run test as `python3 manage.py test <app_name>`

```
python3 manage.py test polls
```

- TO-DO: tests for ResultsView.

    * test_question_not_exist
    * test_future_question
    * test_past_question

- TO-DO: tests for Questions without Choices.

---
---

# Bibliography

- [Curso Django Platzi 2022](https://platzi.com/cursos/django/)

- [My own note taking about python](https://github.com/dcarolinahdev/notes/blob/master/python.md)

- [My own note taking about django](https://github.com/dcarolinahdev/notes/blob/master/django.md)