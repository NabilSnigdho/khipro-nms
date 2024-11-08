from juktoborno import mapping as juktoborno_unsorted
import chars


def sort_by_key_len(x):
    return sorted(x, key=lambda item: (-len(item[0])))


juktoborno = sort_by_key_len(juktoborno_unsorted)

shor = sort_by_key_len(
    [
        ("of", "অ"),
        ("af", "আ"),
        ("if", "ই"),
        ("iif", "ঈ"),
        ("uf", "উ"),
        ("uuf", "ঊ"),
        ("wf", "ঋ"),
        ("ef", "এ"),
        ("oif", "ই"),
        ("oof", "ও"),
        ("ouf", "উ"),
        ("aef", "অ্যা"),
    ]
)

byanjon = sort_by_key_len(
    [
        ("k", "ক"),
        ("kh", "খ"),
        ("g", "গ"),
        ("gh", "ঘ"),
        ("ng", "ঙ"),
        ("c", "চ"),
        ("ch", "ছ"),
        ("j", "জ"),
        ("jh", "ঝ"),
        ("nff", "ঞ"),
        ("tf", "ট"),
        ("tff", "ঠ"),
        ("df", "ড"),
        ("dff", "ঢ"),
        ("nf", "ণ"),
        ("t", "ত"),
        ("th", "থ"),
        ("d", "দ"),
        ("dh", "ধ"),
        ("n", "ন"),
        ("p", "প"),
        ("ph", "ফ"),
        ("b", "ব"),
        ("v", "ভ"),
        ("m", "ম"),
        ("z", "য"),
        ("r", "র"),
        ("l", "ল"),
        ("sh", "শ"),
        ("sf", "ষ"),
        ("s", "স"),
        ("h", "হ"),
        ("y", "য়"),
        ("rf", "ড়"),
        ("rff", "ঢ়"),
    ]
)

ongko = [
    ("1", "১"),
    ("2", "২"),
    ("3", "৩"),
    ("4", "৪"),
    ("5", "৫"),
    ("6", "৬"),
    ("7", "৭"),
    ("8", "৮"),
    ("9", "৯"),
    ("0", "০"),
]

reph = [("r", "র")]

phola = [("r", "র"), ("z", "য")]

kar = sort_by_key_len(
    [
        ("o", ""),
        ("a", "া"),
        ("i", "ি"),
        ("ii", "ী"),
        ("u", "ু"),
        ("uu", "ূ"),
        ("w", "ৃ"),
        ("e", "ে"),
        ("oi", "ৈ"),
        ("oo", "ো"),
        ("ou", "ৌ"),
        ("ae", "্যা"),
    ]
)

diacritic = sort_by_key_len(
    [
        ("qq", "্"),
        ("xx", "্‌"),
        ("tq", "ৎ"),
        ("x", "ঃ"),
        ("q", "ং"),
        (r"(?<!/)/(?!/)", "ঁ"),
        ("`", chars.ZWNJ),
        ("``", chars.ZWJ),
    ]
)

biram = sort_by_key_len(
    [
        (r"\.", "।"),
        (r"\.\.\.", "..."),
        (r"\.\.", "."),
        (r"\$", "৳"),
    ]
)
