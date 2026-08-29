import sys, pathlib
for p in sys.argv[1:]:
    t = pathlib.Path(p).read_text(encoding='utf-8', errors='replace')
    print('#'*100)
    print('FILE:', p)
    print(t)
    print()
