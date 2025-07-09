from textnode import TextType, TextNode 

def main():
    text_node = TextNode("Sample Text", TextType.LINK, "http://example.com")
    print(text_node)

if __name__ == "__main__":
    main()