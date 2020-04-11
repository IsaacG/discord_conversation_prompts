#!/bin/python

import os
import random
from discord.ext import commands


PROMPTS = [
  "1. What was the last funny video you saw?",
  "2. What do you do to get rid of stress?",
  "3. What is something you are obsessed with?",
  "4. What three words best describe you?",
  "5. What would be your perfect weekend?",
  "6. What’s your favorite number? Why?",
  "7. What are you going to do this weekend?",
  "8. What’s the most useful thing you own?",
  "9. What’s your favorite way to waste time?",
  "10. What do you think of tattoos? Do you have any?",
  "11. Do you have any pets? What are their names?",
  "12. Where did you go last weekend? / What did you do last weekend?",
  "13. What is something popular now that annoys you?",
  "14. What did you do on your last vacation?",
  "15. When was the last time you worked incredibly hard?",
  "16. Are you very active, or do you prefer to just relax in your free time?",
  "17. What do you do when you hang out with your friends?",
  "18. Who is your oldest friend? Where did you meet them?",
  "19. What’s the best / worst thing about your work/school?",
  "20. If you had intro music, what song would it be? Why?",
  "21. What were you really into when you were a kid?",
  "22. If you could have any animal as a pet, what animal would you choose?",
  "23. Have you ever saved an animal’s life? How about a person’s life?",
  "24. If you opened a business, what kind of business would it be?",
  "25. Who is your favorite entertainer (comedian, musician, actor, etc.)?",
  "26. Are you a very organized person?",
  "27. Have you ever given a presentation in front of a large group of people? How did it go?",
  "28. What is the strangest dream you have ever had?",
  "29. What is a controversial opinion you have?",
  "30. Who in your life brings you the most joy?",
  "31. Who had the biggest impact on the person you have become?",
  "32. What is the most annoying habit someone can have?",
  "33. Where is the most beautiful place you have been?",
  "34. Where do you spend most of your free time/day?",
  "35. Who was your best friend in elementary school?",
  "36. How often do you stay up past 3 a.m.?",
  "37. What’s your favorite season? Why?",
  "38. Which is more important, having a great car or a great house? Why?",
  "39. What animal or insect do you wish humans could eradicate?",
  "40. Where is the most beautiful place near where you live?",
  "41. What do you bring with you everywhere you go?",
  "42. How much time do you spend on the internet? What do you usually do?",
  "43. What is the most disgusting habit some people have?",
  "44. Where and when was the most amazing sunset you have ever seen?",
  "46. Where is the worst place you have been stuck for a long time?",
  "47. If you had to change your name, what would your new name be?",
  "48. What is something that really annoys you but doesn’t bother most people?",
  "49. What word or saying from the past do you think should come back?",
  "50. How should success be measured? And by that measurement, who is the most successful person you know?",
  "51. What is your guilty pleasure?",
  "52. Was there ever an event in your life that defied explanation?",
  "53. If you could learn the answer to one question about your future, what would the question be?",
  "54. Has anyone ever saved your life?",
  "55. What benefit do you bring to the group when you hang out with friends?",
  "56. How often do you curse? And what’s your go-to string of curse words?",
  "57. What trends did you follow when you were younger?",
  "58. What do you fear is hiding in the dark?",
  "59. What was the best period of your life so far? What do you think will be the best period of your entire life?",
  "60. What do you do to improve your mood when you are in a bad mood?",
  "61. What is the silliest fear you have?",
  "62. What are some things you want to accomplish before you die?",
  "63. What is the best room in your house? Why?",
  "64. Who is someone popular now that you really like? Why do you like them so much?",
  "65. Where is the best place to take a date?",
  "66. What smell brings back great memories?",
  "67. What's the best pet name you can come up with for a specific type of pet?",
  "68. How often do you help others? Who do you help? How do you help?",
  "69. What are you best at?",
  "70. What makes you nervous?",
  "71. Who is the funniest person you’ve met?",
  "72. What weird or useless talent do you have?",
  "73. What are some strange beliefs that some people have?",
  "74. Who would be the worst person to be stuck in an elevator with? How about the best person to be stuck in an elevator with?",
  "75. What was the best birthday wish or gift you&#8217;ve ever received?",
  "76. What’s the best sitcom past or present?",
  "77. What’s the best show currently on TV?",
  "78. What will be the future of TV shows?",
  "79. How often do you binge watch shows?",
  "80. What cartoons did you watch as a child?",
  "81. What’s the funniest TV series you have seen?",
  "82. Which TV show do you want your life to be like?",
  "83. How have TV shows changed over the years?",
  "84. If you could bring back one TV show that was canceled, which one would you bring back?",
  "85. What do you think about game shows? Do you have a favorite one?",
  "86. What’s the most underrated or overrated TV show?",
  "87. What do you think about reality TV? Why do you think it’s so popular?",
  "88. Do you like reality TV shows? Why or why not? If so, which ones?",
  "89. What is the most overrated movie?",
  "90. What’s your favorite genre of movie?",
  "91. Which do you prefer? Books or movies?",
  "92. What movie scene choked you up the most?",
  "93. Do you like documentaries? Why / why not?",
  "94. What’s the worst movie you have seen recently?",
  "95. What’s the strangest movie you have ever seen?",
  "96. Do you like horror movies? Why or why not?",
  "97. When was the last time you went to a movie theater?",
  "98. What was the last movie you watched? How was it?",
  "99. Do movies have the same power as books to change the world?",
  "100. Do you prefer to watch movies in the theater or in the comfort of your own home?",
  "101. What was the last book you read?",
  "102. What was your favorite book as a child?",
  "103. Do you prefer physical books or ebooks?",
  "104. What is the longest book you’ve read?",
  "105. What book genres do you like to read?",
  "106. How fast do you read?",
  "107. How often do you go to the library?",
  "108. What book has influenced you the most?",
  "109. Do you prefer fiction or nonfiction books?",
  "110. What book has changed one of your long-held opinions?",
  "111. What book has had the biggest effect on the modern world?",
  "112. What was the worst book you had to read for school? How about the best book you had to read for school?",
  "113. Do you think people read more or fewer books now than 50 years ago?",
  "114. Now that indie publishing has become easier, have books gotten better or worse?",
  "115. What was the last song you listened to?",
  "116. What is your favorite movie soundtrack?",
  "117. Do you like classical music?",
  "118. What song always puts you in a good mood?",
  "119. What’s the best way to discover new music?",
  "120. How has technology changed the music industry?",
  "121. Are there any songs that always bring a tear to your eye?",
  "122. What bands or types of music do you listen to when you exercise?",
  "123. Which do you prefer, popular music or relatively unknown music?",
  "124. Do you like going to concerts? Why or why not? What was the last concert you went to?",
  "125. Who was the first band or musician you were really into? Do you still like them?",
  "126. Records, tapes, CDs, MP3s, streaming. Which did you grow up with? What is good and bad about each?",
  "127. What are the three best apps on your phone?",
  "128. What is the most useful app on your phone?",
  "129. What do app makers do that really annoys you?",
  "130. How many apps do you have on your phone?",
  "131. What’s the most frustrating app you have tried?",
  "132. What’s the most addictive mobile game you have played?",
  "133. Which app seemed like magic the first time you used it?",
  "134. What is the strangest app you have heard of or tried?",
  "135. What&#8217;re the best and worst things about the marketplace where you get your apps?",
  "136. Which app has helped society the most? Which one has hurt society the most?",
  "138. How often do you check your phone?",
  "139. Do you text more or call more? Why?",
  "140. What will phones be like in 10 years?",
  "141. What do you wish your phone could do?",
  "142. Do you always have to have the latest phone?",
  "143. What is the most annoying thing about your phone?",
  "144. How do you feel if you accidentally leave your phone at home?",
  "145. What kind of case do you have for your phone? Why did you choose it?",
  "146. What was your first smartphone? How did you feel when you got it?",
  "147. Do you experience phantom vibration? (Feeling your phone vibrate even though it didn’t.)",
  "148. What sports do you like to watch?",
  "149. Who are some of your favorite athletes?",
  "150. Which sports do you like to play?",
  "151. What is the hardest sport to excel at?",
  "152. Who are the 3 greatest athletes of all time?",
  "153. How much time do you spend watching sports in a week?",
  "154. Do athletes deserve the high salaries they receive? Why or why not?",
  "155. What defines a sport? Is fishing a sport? How about video game tournaments?",
  "156. Do you play in any fantasy sports leagues? If so, how into fantasy sports are you?",
  "157. Why do you think sports are common across almost all cultures present and past?",
  "158. Do you play sports video games? Which ones? Is playing the video game or playing the sport more fun? Why?",
  "159. Which sport is the most exciting to watch? Which is the most boring to watch?",
  "160. What restaurant do you eat at most?",
  "161. What’s the worst fast food restaurant?",
  "162. What is the best restaurant in your area?",
  "163. What is the fanciest restaurant you have eaten at?",
  "164. What kind of interior do you like a restaurant to have?",
  "165. What is the worst restaurant you have ever eaten at?",
  "166. If you opened a restaurant, what kind of food would you serve?",
  "167. What is the strangest themed restaurant you have heard of?",
  "168. Would you eat at a restaurant that was really dirty if the food was amazing?",
  "169. What is the most disgusting thing you have heard happened at a restaurant?",
  "170. What was your favorite restaurant when you were a child?",
  "171. Where would you like to travel next?",
  "172. What is the longest plane trip you have taken?",
  "173. What&#8217;s the best way to travel?",
  "174. Where is the most relaxing place you have been?",
  "175. Do you prefer traveling alone or with a group?",
  "176. What do you think of tour group packages?",
  "177. Do you prefer to go off the beaten path when you travel?",
  "178. What was the most overhyped place you&#8217;ve traveled to?",
  "179. Have you traveled to any different countries? Which ones?",
  "180. Where is the most awe-inspiring place you have been?",
  "181. What&#8217;s the best thing about traveling? How about the worst thing?",
  "182. What is the worst hotel you have stayed at? How about the best hotel?",
  "183. How do you think traveling to a lot of different countries changes a person?",
  "184. Talk about some of the interesting people you have met while traveling.",
  "185. What do you think of staycations? (Vacationing and seeing tourist attractions where you live.)",
  "186. Where do you get your recommendations for what to do and where to stay when you travel?",
  "187. What is your favorite piece of technology that you own?",
  "188. What piece of technology is really frustrating to use?",
  "189. What was the best invention of the last 50 years?",
  "190. Does technology simplify life or make it more complicated?",
  "191. Will technology save the human race or destroy it?",
  "192. Which emerging technology are you most excited about?",
  "193. What sci-fi movie or book would you like the future to be like?",
  "194. What do you think the next big technological advance will be?",
  "195. What technology from a science fiction movie would you most like to have?",
  "196. What problems will technology solve in the next 5 years? What problems will it create?",
  "197. What piece of technology would look like magic or a miracle to people in medieval Europe?",
  "198. Can you think of any technology that has only made the world worse? How about a piece of technology that has only made the world better?",
  "199. What is your favorite shirt?",
  "200. Does fashion help society in any way?",
  "201. What old trend is coming back these days?",
  "202. What is a fashion trend you are really glad went away?",
  "203. What is the most comfortable piece of clothing you own?",
  "204. What is the most embarrassing piece of clothing you own?",
  "205. How do clothes change how the opposite sex views a person?",
  "206. Do you care about fashion? What style of clothes do you usually wear?",
  "207. If you didn’t care at all what people thought of you, what clothes would you wear?",
  "208. What is the best pair of shoes you have ever owned? Why were they so good?",
  "209. Who do you think has the biggest impact on fashion trends: actors and actresses, musicians, fashion designers, or consumers?",
  "210. What personal goals do you have?",
  "211. What are your goals for the next two years?",
  "212. How have your goals changed over your life?",
  "213. How much do you plan for the future?",
  "214. How do you plan to make the world a better place?",
  "215. What are some goals you have already achieved?",
  "216. What do you hope to achieve in your professional life?",
  "217. Have your parents influenced what goals you have?",
  "218. Do you usually achieve the goals you set? Why or why not?",
  "219. What is the best way to stay motivated and complete goals?",
  "220. What are some goals you have failed to accomplish?",
  "221. What is the craziest, most outrageous thing you want to achieve?",
  "222. When do you want to retire? What do you want to do when you retire?",
  "223. Do you prefer summer or winter activities?",
  "224. What do you like to do in the spring?",
  "225. Did your family take seasonal vacations?",
  "226. Which do you prefer, fall or spring?",
  "227. Which season are you most active in?",
  "228. What’s the most refreshing thing on a hot summer day?",
  "229. What’s the best thing to do on a cold winter day?",
  "230. Where is the nicest place you have been to in fall?",
  "231. What is your favorite thing to eat or drink in winter?",
  "232. Is it better to live where there are four seasons or where one season takes up most of the year?",
  "233. What is the biggest holiday for your family?",
  "234. What is your favorite holiday?",
  "235. What holidays have been over-commercialized?",
  "236. Do you wish there were more or fewer holidays? Why?",
  "237. What do you know about the history of some holidays?",
  "238. What kinds of food do you usually eat on your favorite holiday?",
  "239. If you had to get rid of a holiday, which would you get rid of? Why?",
  "240. Does having a day off for a holiday increase or decrease productivity at work?",
  "241. If some of the lesser-known holidays were commercialized, what would the commercialization look like?",
  "242. If you could make a holiday, what would it be like? What traditions would it have? What would people eat on your holiday?",
  "243. What do you think of online education?",
  "244. What do you think of standardized tests?",
  "245. Are bigger or smaller schools better?",
  "246. Is teaching a skill that can be taught?",
  "247. What will the future of education be?",
  "248. What do you think of homeschooling?",
  # "249. How can governments make education more efficient?",
  "250. How has the education you received changed your life?",
  "251. How can technology improve education? Can it hurt education?",
  "252. What or who has taught you most of the information you use regularly?",
  "253. What are some good and bad things about the education system in your country?",
  "254. What is your favorite cuisine or type of food?",
  "255. What foods do you absolutely hate?",
  "256. What do you think of buffets?",
  "257. When was the last time you had a food fight?",
  "258. What food looks disgusting but tastes delicious?",
  "259. What do you get every time you go grocery shopping?",
  "260. If your life was a meal, what would kind of meal would it be?",
  "261. What would you want your last meal to be if you were on death row?",
  "262. What food do you know you shouldn’t eat but can’t stop yourself?",
  "263. Do you like spicy food? Why or why not? What is the spiciest thing you have ever eaten?",
  # "264. Does the government have a place in regulating food? To what extent should government regulate food?",
  "265. When people make mistakes about food (especially foreign food), do you feel the need to correct them?",
  "266. If your mind were an island, what would it look like?",
  "267. What flavor of ice cream do you wish existed?",
  "268. If you had a personal mascot, what would your mascot be?",
  "269. If you were a king/queen, what would your throne look like?",
  "270. Time freezes for everyone but you for one day. What do you do?",
  "271. You have to relive one day of your life forever. Which day do you choose?",
  "272. What does your own personal hell look like? How about your own personal heaven?",
  "273. You find a remote that can rewind, fast forward, stop, and start time. What do you do with it?",
  "274. If you could call up anyone in the world and have a one-hour conversation, who would you call?",
  "275. The world has become infested with rabid dogs with the intelligence of a 5-year-old, where do you hole up to survive the “a-pup-calypse”?",
  "276. A portal to another world opens in front of you. You don’t know how long it will stay open or if you’ll be able to get back after you go through. What do you do?",
]


class Prompts(commands.Cog):
  """Serve up conversation prompts."""

  qualified_name = 'Conversation Prompter'

  @commands.command()
  async def prompt(self, ctx, *args):
    await ctx.send(random.choice(PROMPTS))


def main():
  bot = commands.Bot(command_prefix='!')
  bot.add_cog(Prompts())
  bot.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
  main()

# vim:ts=2:sw=2:expandtab
