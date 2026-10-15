# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

tweets = []
years = range(2009, 2019)
for year in range(2009, 2019):
    with open(f'master_{year}.json', encoding='utf-8') as f:
        tweets.extend(json.load(f))
print(len(tweets))


def get_message(tweet):
    if 'full_text' in tweet:
        return tweet['full_text']
    return tweet['text']


phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news', 'wall', 'america', 'jobs']

counts = {}
for phrase in phrases:
    counts[phrase] = 0

for tweet in tweets:
    message = get_message(tweet).lower()
    for phrase in phrases:
        if phrase in message:
            counts[phrase] += 1

for phrase in sorted(phrases):
    print(phrase, counts[phrase])

total = len(tweets)
percents = {}
for phrase in phrases:
    percents[phrase] = counts[phrase] / total * 100

lines = ['| phrase            | percent of tweets |',
         '| ----------------- | ----------------- |']
for phrase in sorted(phrases):
    value = f'{percents[phrase]:05.2f}'
    lines.append(f'| {phrase:>17} | {value:<17} |')
print()
print('\n'.join(lines))

names = sorted(phrases)
values = [percents[name] for name in names]
plt.figure(figsize=(8, 5))
plt.barh(names, values)
plt.xlabel('Percent of tweets containing the phrase')
plt.title('Phrases in the tweet archive')
plt.tight_layout()
plt.savefig('tweets.png')