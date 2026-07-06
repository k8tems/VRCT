"""Language table used by transcription components.

Maps a display language and country to engine-specific language codes.
"""

transcription_lang = {
    "Afrikaans":{
        "South Africa":{
            "Google": "af-ZA",
            "Whisper": "af",
            "Qwen": "af",
        },
    },
    "Albanian":{
        "Albania":{
            "Google": "sq-AL",
            "Whisper": "sq",
            "Qwen": "sq",
        },
    },
    "Amharic":{
        "Ethiopia":{
            "Google": "am-ET",
            "Whisper": "am",
            "Qwen": "am",
        },
    },
    "Arabic":{
        "Algeria":{
            "Google": "ar-DZ",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Bahrain":{
            "Google": "ar-BH",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Egypt":{
            "Google": "ar-EG",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Israel":{
            "Google": "ar-IL",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Iraq":{
            "Google": "ar-IQ",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Jordan":{
            "Google": "ar-JO",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Kuwait":{
            "Google": "ar-KW",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Lebanon":{
            "Google": "ar-LB",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Mauritania":{
            "Google": "ar-MR",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Morocco":{
            "Google": "ar-MA",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Oman":{
            "Google": "ar-OM",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Qatar":{
            "Google": "ar-QA",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Saudi Arabia":{
            "Google": "ar-SA",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Palestine":{
            "Google": "ar-PS",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Syria":{
            "Google": "ar-SY",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Tunisia":{
            "Google": "ar-TN",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "United Arab Emirates":{
            "Google": "ar-AE",
            "Whisper": "ar",
            "Qwen": "ar",
        },
        "Yemen":{
            "Google": "ar-YE",
            "Whisper": "ar",
            "Qwen": "ar",
        },
    },
    "Armenian": {
        "Armenia": {
            "Google": "hy-AM",
            "Whisper": "hy",
            "Qwen": "hy",
        },
    },
    "Azerbaijani": {
        "Azerbaijan": {
            "Google": "az-AZ",
            "Whisper": "az",
            "Qwen": "az",
        },
    },
    "Basque":{
        "Spain":{
            "Google": "eu-ES",
            "Whisper": "eu",
            "Qwen": "eu",
        },
    },
    "Bengali":{
        "Bangladesh":{
            "Google": "bn-BD",
            "Whisper": "bn",
            "Qwen": "bn",
        },
        "India":{
            "Google": "bn-IN",
            "Whisper": "bn",
            "Qwen": "bn",
        },
    },
    "Bosnian":{
        "Bosnia and Herzegovina":{
            "Google": "bs-BA",
            "Whisper": "bs",
            "Qwen": "bs",
        }
    },
    "Bulgarian":{
        "Bulgaria":{
            "Google": "bg-BG",
            "Whisper": "bg",
            "Qwen": "bg",
        },
    },
    "Burmese":{
        "Myanmar":{
            "Google": "my-MM",
            "Whisper": "my",
            "Qwen": "my",
        },
    },
    "Catalan":{
        "Spain":{
            "Google": "ca-ES",
            "Whisper": "ca",
            "Qwen": "ca",
        },
    },
    "Chinese Simplified":{
        "China":{
            "Google": "cmn-Hans-CN",
            "Whisper": "zh",
            "Qwen": "zh",
        },
        "Hong Kong":{
            "Google": "cmn-Hans-HK",
            "Whisper": "zh",
            "Qwen": "zh",
        },
    },
    "Chinese Traditional":{
        "Taiwan":{
            "Google": "cmn-Hant-TW",
            "Whisper": "zh",
            "Qwen": "zh",
        },
        "Hong Kong":{
            "Google": "yue-Hant-HK",
            "Whisper": "yue",
            "Qwen": "yue",
        },
    },
    "Croatian":{
        "Croatia":{
            "Google": "hr-HR",
            "Whisper": "hr",
            "Qwen": "hr",
        },
    },
    "Czech":{
        "Czech Republic":{
            "Google": "cs-CZ",
            "Whisper": "cs",
            "Qwen": "cs",
        },
    },
    "Danish":{
        "Denmark":{
            "Google": "da-DK",
            "Whisper": "da",
            "Qwen": "da",
        },
    },
    "Dutch":{
        "Belgium":{
            "Google": "nl-BE",
            "Whisper": "nl",
            "Qwen": "nl",
        },
        "Netherlands":{
            "Google": "nl-NL",
            "Whisper": "nl",
            "Qwen": "nl",
        },
    },
    "English": {
        "Australia":{
            "Google": "en-AU",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Canada":{
            "Google": "en-CA",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Ghana":{
            "Google": "en-GH",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Hong Kong":{
            "Google": "en-HK",
            "Whisper": "en",
            "Qwen": "en",
        },
        "India":{
            "Google": "en-IN",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Ireland":{
            "Google": "en-IE",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Kenya":{
            "Google": "en-KE",
            "Whisper": "en",
            "Qwen": "en",
        },
        "New Zealand":{
            "Google": "en-NZ",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Nigeria":{
            "Google": "en-NG",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Philippines":{
            "Google": "en-PH",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Singapore":{
            "Google": "en-SG",
            "Whisper": "en",
            "Qwen": "en",
        },
        "South Africa":{
            "Google": "en-ZA",
            "Whisper": "en",
            "Qwen": "en",
        },
        "Tanzania":{
            "Google": "en-TZ",
            "Whisper": "en",
            "Qwen": "en",
        },
        "United Kingdom":{
            "Google": "en-GB",
            "Whisper": "en",
            "Qwen": "en",
        },
        "United States":{
            "Google": "en-US",
            "Whisper": "en",
            "Qwen": "en",
        },
    },
    "Estonian":{
        "Estonia":{
            "Google": "et-EE",
            "Whisper": "et",
            "Qwen": "et",
        },
    },
    "Filipino":{
        "Philippines":{
            "Google": "fil-PH",
            "Whisper": "tl",
            "Qwen": "tl",
        },
    },
    "Finnish":{
        "Finland":{
            "Google": "fi-FI",
            "Whisper": "fi",
            "Qwen": "fi",
        },
    },
    "French":{
        "Belgium":{
            "Google": "fr-BE",
            "Whisper": "fr",
            "Qwen": "fr",
        },
        "Canada":{
            "Google": "fr-CA",
            "Whisper": "fr",
            "Qwen": "fr",
        },
        "France":{
            "Google": "fr-FR",
            "Whisper": "fr",
            "Qwen": "fr",
        },
        "Switzerland":{
            "Google": "fr-CH",
            "Whisper": "fr",
            "Qwen": "fr",
        },
    },
    "Galician":{
        "Spain":{
            "Google": "gl-ES",
            "Whisper": "gl",
            "Qwen": "gl",
        },
    },
    "Georgian":{
        "Georgia":{
            "Google": "ka-GE",
            "Whisper": "ka",
            "Qwen": "ka",
        },
    },
    "German":{
        "Austria":{
            "Google": "de-AT",
            "Whisper": "de",
            "Qwen": "de",
        },
        "Germany":{
            "Google": "de-DE",
            "Whisper": "de",
            "Qwen": "de",
        },
        "Switzerland":{
            "Google": "de-CH",
            "Whisper": "de",
            "Qwen": "de",
        },
    },
    "Greek":{
        "Greece":{
            "Google": "el-GR",
            "Whisper": "el",
            "Qwen": "el",
        },
    },
    "Gujarati":{
        "India":{
            "Google": "gu-IN",
            "Whisper": "gu",
            "Qwen": "gu",
        },
    },
    "Hebrew":{
        "Israel":{
            "Google": "iw-IL",
            "Whisper": "he",
            "Qwen": "he",
        },
    },
    "Hindi": {
        "India":{
            "Google": "hi-IN",
            "Whisper": "hi",
            "Qwen": "hi",
        },
    },
    "Hungarian":{
        "Hungary":{
            "Google": "hu-HU",
            "Whisper": "hu",
            "Qwen": "hu",
        },
    },
    "Icelandic":{
        "Iceland":{
            "Google": "is-IS",
            "Whisper": "is",
            "Qwen": "is",
        },
    },
    "Indonesian":{
        "Indonesia":{
            "Google": "id-ID",
            "Whisper": "id",
            "Qwen": "id",
        },
    },
    "Italian":{
        "Italy":{
            "Google": "it-IT",
            "Whisper": "it",
            "Qwen": "it",
        },
        "Switzerland":{
            "Google": "it-CH",
            "Whisper": "it",
            "Qwen": "it",
        },
    },
    "Japanese":{
        "Japan":{
            "Google": "ja-JP",
            "Whisper": "ja",
            "Qwen": "ja",
        },
    },
    # "Javanese":{
    #     "Indonesia":{
    #         "Google": "jv-ID",
    #     },
    # },
    "Kannada":{
        "India":{
            "Google": "kn-IN",
            "Whisper": "kn",
            "Qwen": "kn",
        },
    },
    "Kazakh":{
        "Kazakhstan":{
            "Google": "kk-KZ",
            "Whisper": "kk",
            "Qwen": "kk",
        },
    },
    "Khmer":{
        "Cambodia":{
            "Google": "km-KH",
            "Whisper": "km",
            "Qwen": "km",
        },
    },
    # "Kinyarwanda":{
    #     "rwanda":{
    #         "Google": "rw-RW",
    #     },
    # },
    "Korean":{
        "South Korea":{
            "Google": "ko-KR",
            "Whisper": "ko",
            "Qwen": "ko",
        },
    },
    "Lao":{
        "Laos":{
            "Google": "lo-LA",
            "Whisper": "lo",
            "Qwen": "lo",
        },
    },
    "Latvian":{
        "Latvia":{
            "Google": "lv-LV",
            "Whisper": "lv",
            "Qwen": "lv",
        },
    },
    "Lithuanian":{
        "Lithuania":{
            "Google": "lt-LT",
            "Whisper": "lt",
            "Qwen": "lt",
        },
    },
    "Macedonian":{
        "North Macedonia":{
            "Google": "mk-MK",
            "Whisper": "mk",
            "Qwen": "mk",
        },
    },
    "Malay":{
        "Malaysia":{
            "Google": "ms-MY",
            "Whisper": "ms",
            "Qwen": "ms",
        },
    },
    "Malayalam":{
        "India":{
            "Google": "ml-IN",
            "Whisper": "ml",
            "Qwen": "ml",
        },
    },
    "Mongolian":{
        "Mongolia":{
            "Google": "mn-MN",
            "Whisper": "mn",
            "Qwen": "mn",
        },
    },
    "Nepali":{
        "Nepal":{
            "Google": "ne-NP",
            "Whisper": "ne",
            "Qwen": "ne",
        },
    },
    "Norwegian":{
        "Norway":{
            "Google": "no-NO",
            "Whisper": "no",
            "Qwen": "no",
        },
    },
    "Persian":{
        "Iran":{
            "Google": "fa-IR",
            "Whisper": "fa",
            "Qwen": "fa",
        },
    },
    "Polish":{
        "Poland":{
            "Google": "pl-PL",
            "Whisper": "pl",
            "Qwen": "pl",
        },
    },
    "Portuguese":{
        "Brazil":{
            "Google": "pt-BR",
            "Whisper": "pt",
            "Qwen": "pt",
        },
        "Portugal":{
            "Google": "pt-PT",
            "Whisper": "pt",
            "Qwen": "pt",
        },
    },
    # "Punjabi":{
    #     "India":{
    #         "Google": "pa-Guru-IN",
    #     },
    # },
    "Romanian":{
        "Romania":{
            "Google": "ro-RO",
            "Whisper": "ro",
            "Qwen": "ro",
        },
    },
    "Russian":{
        "Russia":{
            "Google": "ru-RU",
            "Whisper": "ru",
            "Qwen": "ru",
        },
    },
    "Serbian":{
        "Serbia":{
            "Google": "sr-RS",
            "Whisper": "sr",
            "Qwen": "sr",
        },
    },
    "Sinhala":{
        "Sri Lanka":{
            "Google": "si-LK",
            "Whisper": "si",
            "Qwen": "si",
        },
    },
    "Slovak":{
        "Slovakia":{
            "Google": "sk-SK",
            "Whisper": "sk",
            "Qwen": "sk",
        },
    },
    "Slovenian":{
        "Slovenia":{
            "Google": "sl-SI",
            "Whisper": "sl",
            "Qwen": "sl",
        },
    },
    # "Sesotho":{
    #     "South Africa":{
    #         "Google": "st-ZA",
    #     },
    # },
    "Spanish":{
        "Argentina":{
            "Google": "es-AR",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Bolivia":{
            "Google": "es-BO",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Chile":{
            "Google": "es-CL",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Colombia":{
            "Google": "es-CO",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Costa Rica":{
            "Google": "es-CR",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Dominican Republic":{
            "Google": "es-DO",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Ecuador":{
            "Google": "es-EC",
            "Whisper": "es",
            "Qwen": "es",
        },
        "El Salvador":{
            "Google": "es-SV",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Guatemala":{
            "Google": "es-GT",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Honduras":{
            "Google": "es-HN",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Mexico":{
            "Google": "es-MX",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Nicaragua":{
            "Google": "es-NI",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Panama":{
            "Google": "es-PA",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Paraguay":{
            "Google": "es-PY",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Peru":{
            "Google": "es-PE",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Puerto Rico":{
            "Google": "es-PR",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Spain":{
            "Google": "es-ES",
            "Whisper": "es",
            "Qwen": "es",
        },
        "United States":{
            "Google": "es-US",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Uruguay":{
            "Google": "es-UY",
            "Whisper": "es",
            "Qwen": "es",
        },
        "Venezuela":{
            "Google": "es-VE",
            "Whisper": "es",
            "Qwen": "es",
        },
    },
    "Sundanese":{
        "Indonesia":{
            "Google": "su-ID",
            "Whisper": "su",
            "Qwen": "su",
        },
    },
    "Swahili":{
        "Kenya":{
            "Google": "sw-KE",
            "Whisper": "sw",
            "Qwen": "sw",
        },
        "Tanzania":{
            "Google": "sw-TZ",
            "Whisper": "sw",
            "Qwen": "sw",
        },
    },
    # "Swazi":{
    #     "Eswatini":{
    #         "Google": "ss-Latn-ZA",
    #     },
    # },
    "Swedish":{
        "Sweden":{
            "Google": "sv-SE",
            "Whisper": "sv",
            "Qwen": "sv",
        },
    },
    "Tamil":{
        "India":{
            "Google": "ta-IN",
            "Whisper": "ta",
            "Qwen": "ta",
        },
        "malaysia":{
            "Google": "ta-MY",
            "Whisper": "ta",
            "Qwen": "ta",
        },
        "Singapore":{
            "Google": "ta-SG",
            "Whisper": "ta",
            "Qwen": "ta",
        },
        "Sri Lanka":{
            "Google": "ta-LK",
            "Whisper": "ta",
            "Qwen": "ta",
        },
    },
    "Telugu":{
        "India":{
            "Google": "te-IN",
            "Whisper": "te",
            "Qwen": "te",
        },
    },
    "Thai":{
        "Thailand":{
            "Google": "th-TH",
            "Whisper": "th",
            "Qwen": "th",
        },
    },
    # "Tsonga":{
    #     "South Africa":{
    #         "Google": "ts-ZA",
    #     },
    # },
    # "Setswana":{
    #     "South Africa":{
    #         "Google": "tn-Latn-ZA",
    #     },
    # },
    "Turkish":{
        "Turkey":{
            "Google": "tr-TR",
            "Whisper": "tr",
            "Qwen": "tr",
        },
    },
    "Ukrainian":{
        "Ukraine":{
            "Google": "uk-UA",
            "Whisper": "uk",
            "Qwen": "uk",
        },
    },
    "Urdu":{
        "India":{
            "Google": "ur-IN",
            "Whisper": "ur",
            "Qwen": "ur",
        },
        "Pakistan":{
            "Google": "ur-PK",
            "Whisper": "ur",
            "Qwen": "ur",
        },
    },
    "Uzbek":{
        "Uzbekistan":{
            "Google": "uz-UZ",
            "Whisper": "uz",
            "Qwen": "uz",
        },
    },
    # "Venda":{
    #     "South Africa":{
    #         "Google": "ve-ZA",
    #     },
    # },
    "Vietnamese":{
        "Vietnam":{
            "Google": "vi-VN",
            "Whisper": "vi",
            "Qwen": "vi",
        },
    },
    # "Xhosa":{
    #     "South Africa":{
    #         "Google": "xh-ZA",
    #     },
    # },
    # "Zulu":{
    #     "South Africa":{
    #         "Google": "zu-ZA",
    #     },
    # },
}