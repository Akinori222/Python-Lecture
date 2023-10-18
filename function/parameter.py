def func(first, second, third="3"):  # parameter デフォルト指定可能（キーワードパラメータ）指定しない（ポジショナルパラメータ）
    print(f"first:{first}, second:{second},third:{third}")

func("1", "2", "33")  # argument

func("1", third="3", second="2")