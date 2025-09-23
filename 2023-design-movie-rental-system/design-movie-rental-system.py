class MovieRentingSystem:
    """
    A system to manage movie rentals across multiple shops, tracking movie availability, prices,
    and rented movies. Uses SortedList for efficient retrieval of cheapest available movies and
    rented movie records.

    Attributes:
        price_records (dict): Maps (movie, shop) tuple to the rental price.
        movies_records_on_stock (defaultdict): Maps movie to a SortedList of (price, shop) tuples.
        rented (SortedList): Stores (shop, movie, price) tuples for currently rented movies.
    """
    
    def __init__(self, n: int, entries: List[List[int]]):
        """
        Initializes the MovieRentingSystem with n shops and a list of entries.

        Args:
            n (int): Number of shops (not directly used but provided in problem context).
            entries (List[List[int]]): List of [shop, movie, price] entries.

        Time Complexity: O(E * log E), where E is the number of entries, due to inserting
                         into SortedList for each entry.
        Space Complexity: O(E) for storing price records and movie stock records.
        """
        # Dictionary to store (movie, shop) -> price mappings
        self.price_records = {} 
        # defaultdict of SortedList to store (price, shop) for each movie
        self.movies_records_on_stock = defaultdict(SortedList)
        # Populate price records and movie stock
        for shop, movie, price in entries:
            self.price_records[(movie, shop)] = price
            self.movies_records_on_stock[movie].add((price, shop))
        # SortedList to track rented movies as (shop, movie, price)
        self.rented = SortedList()

    def search(self, movie: int) -> List[int]:
        """
        Returns up to 5 shops with the lowest prices for a given movie, in ascending order.

        Args:
            movie (int): The movie to search for.

        Returns:
            List[int]: List of up to 5 shop IDs where the movie is available, sorted by price.

        Time Complexity: O(1) to access the SortedList slice, since SortedList maintains order.
        Space Complexity: O(1) for returning up to 5 shop IDs.
        """
        # Return shop IDs from the first 5 (price, shop) pairs for the movie
        return [shop for _, shop in self.movies_records_on_stock[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        """
        Rents a movie from a specific shop, removing it from stock and adding to rented list.

        Args:
            shop (int): The shop ID.
            movie (int): The movie ID.

        Time Complexity: O(log N), where N is the number of entries for the movie in
                         movies_records_on_stock (for removal) or rented movies (for insertion).
        Space Complexity: O(1) for updating the data structures.
        """
        # Get the price for the (movie, shop) pair
        price = self.price_records[(movie, shop)]
        # Remove the movie from available stock
        self.movies_records_on_stock[movie].remove((price, shop))
        # Add to rented movies list
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Returns a rented movie to the shop, adding it back to stock and removing from rented.

        Args:
            shop (int): The shop ID.
            movie (int): The movie ID.

        Time Complexity: O(log N), where N is the number of entries for the movie in
                         movies_records_on_stock (for insertion) or rented movies (for removal).
        Space Complexity: O(1) for updating the data structures.
        """
        # Get the price for the (movie, shop) pair
        price = self.price_records[(movie, shop)]
        # Add the movie back to available stock
        self.movies_records_on_stock[movie].add((price, shop))
        # Remove from rented movies list
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        """
        Returns up to 5 currently rented movies, sorted by shop ID and then movie ID.

        Returns:
            List[List[int]]: List of [shop, movie] pairs for up to 5 rented movies.

        Time Complexity: O(1) to access the SortedList slice, since SortedList maintains order.
        Space Complexity: O(1) for returning up to 5 pairs.
        """
        # Return [shop, movie] pairs from the first 5 rented records
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()