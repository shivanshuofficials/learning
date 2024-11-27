def func():
    try:
      a = int(input("Enter a number:"))
      print(a)
      return

    except Exception as e:
        print("invalid")

    finally:
        print("finally")

func()