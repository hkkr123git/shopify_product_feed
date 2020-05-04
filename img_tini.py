import tinify
tinify.key = "zhlZJbqJSZ1T74sYx3BX98gmyvgJxnh6"

source = tinify.from_file("unoptimized.jpg")
source.to_file("optimized.jpg")