Class Node:
    Data
    Next

Class Queue:
    Head
    Tail

    Function is_empty():        # dependent on Queue
        Return True if Head is None else False

    Function enqueue(Data):     # dependent on Queue
        NewNode = Node(Data)

        If Tail is not None:
            Tail.Next = NewNode

        Tail = NewNode

        If Head is None:
            Head = NewNode

    Function dequeue():         # dependent on Queue
        If is_empty() is True:
            Raise Exception "Queue is empty"

        Value = Head.Data
        Head = Head.Next

        If Head is None:
            Tail = None

        Return Value
