# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class PreviewRequest(DefaultObject):
    @property
    @serializable(name="text", type=unicode)
    def text(self):
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="languageCode", type=unicode)
    def language_code(self):
        return self.get_field_value("language_code")

    @language_code.setter
    def language_code(self, language_code):
        self.set_field_value("language_code", language_code)

    def set_language_code(self, language_code):
        self.language_code = language_code
        return self

    @property
    @serializable(name="transliteration", type=unicode)
    def transliteration(self):
        return self.get_field_value("transliteration")

    @transliteration.setter
    def transliteration(self, transliteration):
        self.set_field_value("transliteration", transliteration)

    def set_transliteration(self, transliteration):
        self.transliteration = transliteration
        return self