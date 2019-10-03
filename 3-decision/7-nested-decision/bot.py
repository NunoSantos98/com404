print("What type of cover does the book have?")
cover = input()

if(cover=="soft"): 
    print("Is the book perfect-bound?")
    book_bound=input()

    if(book_bound=="yes"):
        print("Soft cover, perfect bound books are very popular!")

elif(cover=="hard"):
    print("Books with hard covers can be more expensive!")
