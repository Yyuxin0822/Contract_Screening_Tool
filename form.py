from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), FileAllowed(['docx'], 'docx only!')])
    submit = SubmitField('Upload File')
    
    #restrict file to .docx
    #file = FileField('File', validators=[FileRequired(), FileAllowed(['docx'], 'docx only!')])