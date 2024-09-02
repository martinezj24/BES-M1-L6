
def find_file(file_system, target):
    for item in file_system:
        if isinstance(item, list): 
            find_file(item, target)
        elif item == target:
            print("big HOORAY")
            return  #Stops the search once target is acquired



file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

print(find_file(file_system, target))

