# -*- coding:utf-8 -*-
import os
import pandas as pd
from typing import List, Tuple, Dict

def clean_and_split(text: str) -> List[str]:
    text = (
        text.replace(",", " ")
        .replace("+", " ")
        .replace("-", " ")
        .replace(":", " ")
        .replace("(", " ")
        .replace(")", " ")
        .replace(" ", " ")
        .replace("    ", " ")
        .replace("   ", " ")
        .replace("  ", " ")
        .strip()
    )
    return text.split(" ")

def generate_ngrams(words: List[str], n: int) -> List[str]:
    return [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]

def extract_ngrams(text: str, min_n: int = 3, max_n: int = 5) -> List[str]:
    words = clean_and_split(text)
    ngrams = []
    for n in range(min_n, max_n + 1):
        ngrams.extend(generate_ngrams(words, n))
    return list(set(ngrams))

def calculate_ngram_frequency(df: pd.DataFrame, col_name: str) -> Dict[str, int]:
    freq = {}
    for ngrams in df[col_name]:
        for ngram in ngrams:
            if ngram in freq:
                freq[ngram] += 1
            else:
                freq[ngram] = 1
    return freq

def main():
    input_file = r".\输入数据.xlsx"
    output_file = "./输出结果.xlsx"

    print("正在打开表")
    df = pd.read_excel(input_file)

    print("正在计算")
    df["高频属性词"] = df["Title"].apply(lambda x: extract_ngrams(str(x)))

    ngram_freq = calculate_ngram_frequency(df, "高频属性词")

    df["高频属性词"] = df["高频属性词"].apply(lambda x: max(x, key=lambda y: ngram_freq.get(y, 0)) if x else '/')
    df["词频"] = df["高频属性词"].apply(lambda x: ngram_freq.get(x, 0))

    ngram_df = pd.DataFrame({"高频词": list(ngram_freq.keys()), "频次": list(ngram_freq.values())})

    # Add a new column to ngram_df with the number of words in each n-gram
    ngram_df["词数"] = ngram_df["高频词"].apply(lambda x: len(x.split(" ")))

    print("正在保存")
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name="原表", index=False)
        ngram_df.to_excel(writer, sheet_name="高频词", index=False)

if __name__ == "__main__":
    main()
