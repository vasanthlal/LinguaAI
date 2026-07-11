from sqlalchemy.orm import Session

from app.models.language import Language


def seed_languages(db: Session):

    languages = [
        {
            "name": "English",
            "code": "en",
            "native_name": "English",
            "country_code": "GB",
        },
        {
            "name": "Japanese",
            "code": "ja",
            "native_name": "日本語",
            "country_code": "JP",
        },
        {
            "name": "German",
            "code": "de",
            "native_name": "Deutsch",
            "country_code": "DE",
        },
        {
            "name": "French",
            "code": "fr",
            "native_name": "Français",
            "country_code": "FR",
        },
        {
            "name": "Spanish",
            "code": "es",
            "native_name": "Español",
            "country_code": "ES",
        },
        {
            "name": "Hindi",
            "code": "hi",
            "native_name": "हिन्दी",
            "country_code": "IN",
        },
        {
            "name": "Tamil",
            "code": "ta",
            "native_name": "தமிழ்",
            "country_code": "IN",
        },
        {
            "name": "Malayalam",
            "code": "ml",
            "native_name": "മലയാളം",
            "country_code": "IN",
        },
        {
            "name": "Arabic",
            "code": "ar",
            "native_name": "العربية",
            "country_code": "SA",
        },
        {
            "name": "Chinese",
            "code": "zh",
            "native_name": "中文",
            "country_code": "CN",
        },
    ]

    for language in languages:

        exists = (
            db.query(Language)
            .filter(Language.code == language["code"])
            .first()
        )

        if not exists:
            db.add(Language(**language))

    db.commit()