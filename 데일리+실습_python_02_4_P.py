# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500
steak = 50000
vat = round(50000*0.15)
total = steak + vat

print(f"# 스테이크   {format(steak,',d')}\n# + VAT     {format(vat,',d')}\n# 총계 ₩    {format(total,',d')}")












