"""Random Horoscope Generator, by Michael Sproul."""

import random
from datetime import date, timedelta

import sys
sys.path.append("/home/Admin/Project-2/service3/application")
from application import wordlist
from application import common
#from common import common.choose_from, choose_uniq, sentence_case, ing_to_ed, an



def relationship_s(mood, dirty):
    """Generate a sentence about a relationship."""
    if mood == "good":
        verb = "strengthened"
        talk = "discussion"
    else:
        verb = "strained"
        talk = "argument"

    # Wordlists
    familiar_people = wordlist.wordlist("familiar_people", dirty)
    conversation_topics = wordlist.wordlist("conversation_topics", dirty)

    person = common.choose_from(familiar_people)
    topic = common.choose_from(conversation_topics)
    s = "Your relationship with %s may be %s " % (person, verb)
    s += "as the result of %s about %s" % (common.an(talk), topic)

    return common.sentence_case(s)


def encounter_s(mood, dirty):
    """Generate a few sentences about a meeting with another person."""
    # Sentence 1: The meeting
    familiar_people = wordlist.wordlist("familiar_people", dirty)
    strange_people = wordlist.wordlist("strange_people", dirty)
    locations = wordlist.wordlist("locations", dirty)

    person = common.choose_from(familiar_people, strange_people)
    location = common.choose_from(locations)
    preposition = location[0]
    location = location[1]
    s1 = "You may meet %s %s %s." % (person, preposition, location)

    # Sentence 2: The discussion
    discussions = wordlist.wordlist("neutral_discussions", dirty)
    discussions += wordlist.wordlist("_discussions", dirty, prefix=mood)
    feeling_nouns = wordlist.wordlist("_feeling_nouns", dirty, prefix=mood)
    emotive_nouns = wordlist.wordlist("_emotive_nouns", dirty, prefix=mood)
    conversation_topics = wordlist.wordlist("conversation_topics", dirty)

    discussion = common.choose_from(discussions)
    if random.random() <= 0.5:
        feeling = common.choose_from(feeling_nouns)
        feeling = "feelings of %s" % feeling
    else:
        feeling = common.choose_from(emotive_nouns)
    topic = common.choose_from(conversation_topics)

    s2 = "%s about %s may lead to %s." % (common.an(discussion), topic, feeling)
    s2 = common.sentence_case(s2)
    return "%s %s" % (s1, s2)


def date_prediction_s(mood, dirty):
    """Generate a random prediction sentence containing a date."""
    days_in_future = random.randint(2, 8)
    significant_day = date.today() + timedelta(days=days_in_future)
    month = significant_day.strftime("%B")
    day = significant_day.strftime("%d").lstrip('0')

    r = random.random()

    if r <= 0.5:
        s = "%s %s will be an important day for you" % (month, day)
    elif r <= 0.8:
        s = "Interesting things await you on %s %s" % (month, day)
    else:
        s = "The events of %s %s have the potential to change your life." % (month, day)

    return common.sentence_case(s)


def feeling_statement_s(mood, dirty):
    """Generate a sentence that asserts a mood-based feeling."""
    adjectives = wordlist.wordlist("_feeling_adjs", dirty, prefix=mood)
    degrees = wordlist.wordlist("neutral_degrees", dirty) + wordlist.wordlist("_degrees", dirty, prefix=mood)

    i = random.randint(0,len(adjectives)-1)
    adj = adjectives[i]

    adj = common.ing_to_ed(adj)
    degree = common.choose_from(degrees)

    ending = positive_intensifier if mood == "good" else consolation
    exciting = (mood == "good" and random.random() <= 0.5)
    are = random.choice([" are", "'re"])
    s = "You%s feeling %s %s" % (are, degree, adj)
    s += ending(dirty)
    return common.sentence_case(s, exciting)


def positive_intensifier(dirty):
    """Extend a statement of positive feelings."""
    r = random.random()

    # Increase the probability of not giving a fuck as appropriate.
    dirty_factor = 2 if dirty else 1

    if r <= (0.5/dirty_factor):
        verb = random.choice(["say", "do"])
        return ", and there's nothing anyone can %s to stop you" % verb
    elif r <= (0.95/dirty_factor):
        return ", and you don't care who knows it"
    else:
        return ", and you don't give a fuck"


def consolation(dirty):
    """Provide a consolation for feeling bad."""
    r = random.random()

    if r <= 0.6:
        when = random.choice(["shortly", "soon", "in due time"])
        return ", but don't worry, everything will improve %s" % when
    elif r <= 0.9:
        return ", perhaps you need a change in your life?"
    else:
        return "..."


def warning_s(mood, dirty):
    r = random.random()
    avoid_list = wordlist.wordlist("avoid_list", dirty)
    bad_thing = random.choice(avoid_list)

    if r <= 0.27:
        s = "You would be well advised to avoid %s" % bad_thing
    elif r <= 0.54:
        s = "Avoid %s at all costs" % bad_thing
    elif r <= 0.81:
        s = "Steer clear of %s for a stress-free week"  % bad_thing
    else:
        also_bad = common.choose_uniq({bad_thing}, avoid_list)
        s = "For a peaceful week, avoid %s and %s" % (bad_thing, also_bad)

    return common.sentence_case(s)


def cosmic_implication_s(mood, dirty):
    """Generate a sentence about the influence of a cosmic event."""
    c_event = cosmic_event(dirty)
    prediction_verbs = wordlist.wordlist("prediction_verbs", dirty)
    verb = common.choose_from(prediction_verbs)

    # Bad mood =  End of good, or start of bad
    # Good mood = End of bad, or start of good
    r = random.random()
    beginnings = wordlist.wordlist("beginnings", dirty)
    endings = wordlist.wordlist("endings", dirty)
    if mood == 'bad' and r <= 0.5:
        junction = common.choose_from(beginnings)
        e_event = emotive_event('bad', dirty)
    elif mood == 'bad':
        junction = common.choose_from(endings)
        e_event = emotive_event('good', dirty)
    elif mood == 'good' and r <= 0.5:
        junction = common.choose_from(beginnings)
        e_event = emotive_event('good', dirty)
    else:
        junction = common.choose_from(endings)
        e_event = emotive_event('bad', dirty)

    s = "%s %s the %s of %s" % (c_event, verb, junction, common.an(e_event))
    return common.sentence_case(s)


def cosmic_event(dirty):
    r = random.random()

    planets = wordlist.wordlist("planets", dirty)
    stars = wordlist.wordlist("stars", dirty)
    wanky_events = wordlist.wordlist("wanky_events", dirty)
    aspects = wordlist.wordlist("aspects", dirty)

    if r <= 0.25:
        return random.choice(planets) + " in retrograde"
    elif r <= 0.5:
        c_event = "the " + random.choice(["waxing", "waning"])
        c_event += " of " + common.choose_from(planets, ["the moon"], stars)
        return c_event
    elif r <= 0.6:
        return "the " + random.choice(["New", "Full"]) + " Moon"
    elif r <= 0.75:
        return random.choice(wanky_events)
    else:
        first = common.choose_from(planets, stars, ["Moon"])
        second = common.choose_uniq({first}, planets, stars, ["Moon"])
        return "The %s/%s %s" % (first, second, common.choose_from(aspects))


def emotive_event(mood, dirty):
    """Generate a sentence about a prolonged emotion."""
    feeling_adjs = wordlist.wordlist("_feeling_adjs", dirty, prefix=mood)
    emotive_adjs = wordlist.wordlist("_emotive_adjs", dirty, prefix=mood)
    feeling_nouns = wordlist.wordlist("_feeling_nouns", dirty, prefix=mood)
    emotive_nouns = wordlist.wordlist("_emotive_nouns", dirty, prefix=mood)
    time_periods = wordlist.wordlist("time_periods", dirty)
    time_period = random.choice(time_periods)

    if random.random() <= 0.5:
        adj = common.choose_from(feeling_adjs, emotive_adjs)
        return "%s %s" % (adj, time_period)
    else:
        noun = common.choose_from(feeling_nouns, emotive_nouns)
        return "%s of %s" % (time_period, noun)
    """Generate a sentence about a prolonged emotion."""
    feeling_adjs = wordlist.wordlist("_feeling_adjs", prefix=mood)
    emotive_adjs = wordlist.wordlist("_emotive_adjs", prefix=mood)
    feeling_nouns = wordlist.wordlist("_feeling_nouns", prefix=mood)
    emotive_nouns = wordlist.wordlist("_emotive_nouns", prefix=mood)
    time_periods = wordlist.wordlist("time_periods")
    time_period = random.choice(time_periods)

    if random.random() <= 0.5:
        adj = common.choose_from(feeling_adjs, emotive_adjs)
        return "%s %s" % (adj, time_period)
    else:
        noun = common.choose_from(feeling_nouns, emotive_nouns)
        return "%s of %s" % (time_period, (noun))


def generate(mood, dirty=False):
    """Generate a three to four sentence horoscope."""
    # Pick a mood (usually positive)
    #mood = "good" if random.random() <= 0.8 else "bad"

    c = random.randint(1,2)
    discussion_s = relationship_s if c == 1 else encounter_s
        

    #discussion_s = common.choose_from([relationship_s, encounter_s])
    sentences = [feeling_statement_s, cosmic_implication_s, warning_s, discussion_s]

    # Select 2 or 3 sentences
    k = random.randint(2, 3)
    sentences = random.sample(sentences, k)
    #final_text = " ".join([s(mood, dirty) for s in sentences])
    final_words = []
    print (sentences)
    for sentence in sentences:
        print (sentence)
        final_words.append(sentence(mood,dirty))
    final_text = " ".join(final_words)
    # Optionally add a date prediction
    if random.random() <= 0.5 and k == 2:
        final_text += " " + date_prediction_s(mood, dirty)

    return final_text