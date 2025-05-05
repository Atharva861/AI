def chatbot():
    print("Welcome to BookNest 📚 - Your Online Bookstore Assistant!")
    print("How can I help you today?")
    print("Type '1' to check order status")
    print("Type '2' to search for a book")
    print("Type '3' for return and refund policy")
    print("Type '4' to talk to a human agent")
    print("Type 'exit' to end the chat")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == '1':
            order_id = input("Please enter your Order ID: ")
            print(f"Checking status for Order ID: {order_id}...")
            print("Your order is on the way and will be delivered in 2-3 days.")

        elif user_input == '2':
            book = input("Enter the title or author of the book: ")
            print(f"Searching for '{book}'...")
            print("The book is available. Would you like to add it to your cart?")

        elif user_input == '3':
            print("Our return policy allows returns within 7 days of delivery.")
            print("Refunds are processed within 3-5 business days after return.")

        elif user_input == '4':
            print("Connecting you to a human agent... Please wait.")
            break  # Ending chatbot loop as user is transferred

        elif user_input == 'exit':
            print("Thank you for visiting BookNest! Have a great day!")
            break

        else:
            print("Sorry, I didn't understand that. Please choose an option from the menu.")

chatbot()