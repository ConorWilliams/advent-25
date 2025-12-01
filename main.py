def main():
    with open("data.1.txt", "r") as f:
        data = f.readlines()
        data = [d.strip().replace("R", "+").replace("L", "-") for d in data]
        data = list(map(int, data))

    start = 50
    count = 0

    for elem in data:
        for _ in range(abs(elem)):
            if elem > 0:
                start = (start + 1) % 100
            else:
                start = (start - 1) % 100

            if start == 0:
                count += 1

    print("Count:", count)


if __name__ == "__main__":
    main()
