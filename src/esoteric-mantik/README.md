# 🧩 Esoteric Logic: Deterministic Loop

Bu dizin, projenin felsefi derinliğini teknik bir paradoksla birleştiren "egzotik" bir mantık katmanı içerir.

## 🧠 Neden Brainfuck?

**Brainfuck**, dünyadaki en minimalist ve katı programlama dillerinden biridir. Sadece 8 komut ile (`+`, `-`, `<`, `>`, `[`, `]`, `,`, `.`) her türlü hesaplamayı yapabilir. Bu dilin seçilme sebepleri projenin manifestosu ile doğrudan ilişkilidir:

1.  **Tam Determinizm:** Kodun akışı tamamen mekaniktir; her adım bir öncekinin doğrudan sonucudur. Bu, "Teknolojik Determinizm" döngüsünün en saf halini temsil eder.
2.  **Ontolojik Mekanikleşme:** İnsanın okumasının çok zor, makinenin anlamasının ise saniyeler aldığı bu kod; insanın kendi yarattığı araçların (mekanikleşmenin) içinde nasıl kaybolabileceğini simgeler.
3.  **Paradoks (FITRA):** En katı, en ruhsuz ve en mekanik dille bile olsa, insanın "Fıtrat"ını (Doğasını) ifade etmeye çalışması, Hanif Teknolojinin çıkış arayışını temsil eder.

## 🛠️ Kodun Anatomisi: `deterministic_loop.bf`

Bu dosya, standart bir Brainfuck yorumlayıcısında çalıştırıldığında çıktısında şu kelimeyi üretir:

**`FITRA`**

### Çalıştırma (Python Örneği)

Eğer bir yorumlayıcınız yoksa, aşağıdaki basit Python koduyla çalıştırabilirsiniz:

```python
import sys

def bf(code):
    cells = [0] * 30000
    ptr = 0
    pc = 0
    while pc < len(code):
        c = code[pc]
        if c == '>': ptr += 1
        elif c == '<': ptr -= 1
        elif c == '+': cells[ptr] = (cells[ptr] + 1) % 256
        elif c == '-': cells[ptr] = (cells[ptr] - 1) % 256
        elif c == '.': sys.stdout.write(chr(cells[ptr]))
        elif c == '[':
            if cells[ptr] == 0:
                depth = 1
                while depth > 0:
                    pc += 1
                    if code[pc] == '[': depth += 1
                    elif code[pc] == ']': depth -= 1
        elif c == ']':
            if cells[ptr] != 0:
                depth = 1
                while depth > 0:
                    pc -= 1
                    if code[pc] == ']': depth += 1
                    elif code[pc] == '[': depth -= 1
        pc += 1

with open("deterministic_loop.bf", "r") as f:
    bf(f.read())
```

---

> *"Makineler insanlaşırken, biz en azından kodlarımızda insan fıtratını saklı tutmalıyız."*
