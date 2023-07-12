# scifi-corpus

This is a GPLv3 sci-fi corpus to train LLMs.
Essentially, this means you can use this corpus to do anything you want as long as you make your code freely available to anyone else do whatever they want with it.
Your code must also be licensed as GPLv3. Read more about free software [here](https://www.gnu.org/licenses/rms-why-gplv3.en.html).

⚠️ Currently there are several instructions missing in the dataset, if you want to help head over [here](https://github.com/marimeireles/scifi-corpus/issues/1).
I've decided to release the dataset anyway because I thought it might already be useful for some people.

## general information

### where is the dataset?

Currently, kindly hosted by 🤗 [hugging-face](https://huggingface.co/datasets/elektra/scifi-corpus).

### what does it consists of?

The database consists of a json file formatted in the following manner:

```
    {
        "instruction": "Immersed in the serene depths of the monastery, Nakamura crossed paths with the
                        enigmatic Master Xin, a sage of unparalleled wisdom.",
        "input": "",
        "output": "Within the monastery, Nakamura encountered a sage, an enigmatic figure known as Master
                  Xin. Wise and all-knowing, Master Xin possessed an understanding of the intricate workings
                  of time itself. Through their conversations, Nakamura delved deeper into the altered timeline
                  mysteries and the dangers that lay ahead."
    },
```

The instruction was generated using some language model (sometimes GPT by OpenAI, sometimes Falcon, sometimes Llama) based on the output. The output comes from several
different sources described in the [source](https://github.com/marimeireles/scifi-corpus/new/master?readme#sources) section. The ouput is capped in 500chars. The current dataset contains about 3GB of data.

You will notice that's the exact format the current (2023) LLM models are using for fine-tuning. This is the main purpose of this data set. However, you're free to modify
the data as you wish and change its formatting.
Contributions are very much appreciated, you can check the [projects page](https://github.com/users/marimeireles/projects/1) to learn how to get involved.

## sources

- reddit:
  - r/cyberpunk_stories ✅
  - r/shortscifistories - Script ready
- omdb ✅
- gutenberg ✅
- aooo - Script ready
- specific wikis ([recommended tool](https://www.mediawiki.org/wiki/Manual:Pywikibot)):
  - KOTOR - Needs script
  - SW - Needs script
  - Star Trek - Needs script
- isfdb - Needs script
- [SciFi Stories Text Corpus](https://www.kaggle.com/datasets/jannesklaas/scifi-stories-text-corpus) - Needs work
- [SF Corpus](https://huggingface.co/SF-Corpus) - Needs work

## how to cite

Meireles, M. (2023). Sci-Fi Corpus. ORCID: 0000-0001-9227-9798. Available at: https://huggingface.co/datasets/elektra/scifi-corpus
