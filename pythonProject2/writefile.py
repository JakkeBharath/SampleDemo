with open('sample.txt', 'r') as reader:
    content = reader.readlines()
    print(content)
    reversed(content)
    with open('sample.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)



from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Browser\chromedriver.exe")

driver.get("https://146.205.2.30/")


