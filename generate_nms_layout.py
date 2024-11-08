import pickle
import datetime
import re
import chars
import mappings


def generate_nms_layout(name, version):
    data = {
        "name": name,
        "type": "layout",
        "lang": "Bangla",
        "dic": "Bangla",
        "version": version,
        "modification-time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "phonetic": True,
        "developerName": "nabilsnigdho",
        "developerConctInfo": "Adopted from https://github.com/rank-coder/khipro-m17n",
        "macroTranslate": False,
        "non_zoiner_list": [],
        "ignore_list": [],
        "password": "",
        "github_link": "https://raw.githubusercontent.com/NabilSnigdho/khipro-nms/refs/heads/main/Khipro.nmsLayout",
        "keysToBlock": list(
            map(
                int,
                "41,53,40,43,53,2,55,9,3,16,12,74,4,17,13,78,5,30,18,6,44,31,19,7,45,32,20,8,57,46,33,21,9,47,34,22,10,48,35,23,11,49,36,24,12,50,37,25,13,51,38,26,52,39,27".split(
                    ","
                ),
            )
        ),
        "keyMap": {
            key: val
            for key, val in (
                mappings.juktoborno
                + mappings.ongko
                + [(r"\.([০-৯])", r".\1")]
                + mappings.diacritic
                + mappings.biram
                + mappings.byanjon
                + [
                    ("র([ক-হড়-য়])", "র" + chars.B_HASANTA + r"\1"),
                    ("([ক-হড়-য়])র", r"\1" + chars.B_HASANTA + "র"),
                    ("([ক-হড়-য়])য", r"\1" + chars.B_HASANTA + "য"),
                ]
                + [
                    ("uuff", chars.ZWNJ + chars.B_UU_KAR),
                    ("uff", chars.ZWNJ + chars.B_U_KAR),
                    ("wff", chars.ZWNJ + chars.B_RRI_KAR),
                ]
                + mappings.shor
                + list(
                    map(lambda x: ("([ক-হড়-য়f])" + x[0], r"\1" + x[1]), mappings.kar)
                )
                + list(map(lambda x: (x[0][:-1], x[1]), mappings.shor))
                + [
                    (r"[of]|(?<!;);(?!;)", ""),
                    (";;", ";"),
                    (r"//", "/"),
                ]
            )
        },
    }

    pickle_file_path = f"{name}.nmsLayout"

    with open(pickle_file_path, "wb") as pickle_file:
        pickle.dump(data, pickle_file)

    print(f"Layout {name} has been saved to {pickle_file_path}.")

    return data


data = generate_nms_layout("Khipro", "0.1")


def convert(text: str) -> str:
    for pattern, replacement in data["keyMap"].items():
        text = re.sub(pattern, replacement, text)
    return text


test_cases = {
    "k;b;r": "কবর",
    "kobor": "কবর",
    "som aj": "সম আজ",
    "som faj": "সম াজ",
    "somaj": "সমাজ",
    "hwdoy": "হৃদয়",
    "hwffdoy": "হ‌ৃদয়",
    "aekauntf": "অ্যাকাউন্ট",
    "boi": "বৈ",
    "boif": "বই",
    "bif": "বই",
    "b;i": "বই",
    "bo;i": "বই",
    "kkhrortz": "ক্ষ্রর্ত্য",
    "kore": "করে",
    "//": "/",
    "/": chars.B_CHANDRA,
    ";;": ";",
    ";": "",
}

for eng, bn in test_cases.items():
    c = convert(eng)
    if c != bn:
        print(c)
