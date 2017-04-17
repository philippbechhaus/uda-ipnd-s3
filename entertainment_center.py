import media
import fresh_tomatoes


# ---START Movie Database---

the_dark_knight = media.Movie("The Dark Knight",
                              "With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                              "https://www.youtube.com/watch?v=RWgyKDfFC_U")

room = media.Movie("Room",
                   "Held captive for years in an enclosed space, a woman (Brie Larson) and her young son (Jacob Tremblay) finally gain their freedom, allowing the boy to experience the outside world for the first time.",
                   "http://t1.gstatic.com/images?q=tbn:ANd9GcSu9dR_6oOzsDvAq76vlBqPsyYNHdLw3jRRrmJVb7EBPTQBryV1",
                   "https://www.youtube.com/watch?v=E_Ci-pAL4eE")

interstellar = media.Movie("Interstellar",
                           "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

cloud_atlas = media.Movie("Cloud Atlas",
                          "Actors (Tom Hanks, Halle Berry, Jim Broadbent) take on multiple roles in an epic that spans five centuries. An attorney harbors a fleeing slave on a voyage from the Pacific Islands in 1849; a poor composer in pre-World War II Britain struggles to finish his magnum opus before a past act catches up with him; a genetically engineered worker in 2144 feels the forbidden stirring of human consciousness -- and so on. As souls are born and reborn, they renew their bonds to one another throughout time.",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcQZQhasO56in_vxYDa30rB9tzQg1wk6yKJkkdVoxG43hCJeYuEm",
                          "https://www.youtube.com/watch?v=hWnAqFyaQ5s")

schindlers_list = media.Movie("Schindlers List",
                              "Businessman Oskar Schindler (Liam Neeson) arrives in Krakow in 1939, ready to make his fortune from World War II, which has just started. After joining the Nazi party primarily for political expediency, he staffs his factory with Jewish workers for similarly pragmatic reasons. When the SS begins exterminating Jews in the Krakow ghetto, Schindler arranges to have his workers protected to keep his factory in operation, but soon realizes that in so doing, he is also saving innocent lives.",
                              "http://www.gstatic.com/tv/thumb/movieposters/15227/p15227_p_v8_ah.jpg",
                              "https://www.youtube.com/watch?v=vOoWpTxKJGA")

memento = media.Movie("Memento",
                      "Leonard (Guy Pearce) is tracking down the man who raped and murdered his wife. The difficulty, however, of locating his wife's killer is compounded by the fact that he suffers from a rare, untreatable form of memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
                      "http://www.gstatic.com/tv/thumb/movieposters/28578/p28578_p_v8_af.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

# ---END Movie Database---




# ---Listing movie data---

movies = [the_dark_knight,room,interstellar,cloud_atlas,schindlers_list,memento]



# ---Open Movie Website---

fresh_tomatoes.open_movies_page(movies)
