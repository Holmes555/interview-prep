from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.food_dict = {}
        self.highestRated_food = {}
        for i, cuisine in enumerate(cuisines):
            if cuisine not in self.food_dict:
                self.food_dict[cuisine] = {}
            self.food_dict[cuisine][foods[i]] = ratings[i]
            if cuisine not in self.highestRated_food:
                self.highestRated_food[cuisine] = (foods[i], ratings[i])
            else:
                current_highest = self.highestRated_food[cuisine]
                if ratings[i] > current_highest[1] or (
                    ratings[i] == current_highest[1] and foods[i] < current_highest[0]
                ):
                    self.highestRated_food[cuisine] = (foods[i], ratings[i])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[self.foods.index(food)]
        self.food_dict[cuisine][food] = newRating
        current_highest = self.highestRated_food[cuisine]
        if food == current_highest[0] and newRating < current_highest[1]:
            # need to find new highest
            highest_food = food
            highest_rating = newRating
            for f, r in self.food_dict[cuisine].items():
                if r > highest_rating or (r == highest_rating and f < highest_food):
                    highest_food = f
                    highest_rating = r
            self.highestRated_food[cuisine] = (highest_food, highest_rating)
            return
        if newRating > current_highest[1] or (newRating == current_highest[1] and food < current_highest[0]):
            self.highestRated_food[cuisine] = (food, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.highestRated_food[cuisine][0]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
