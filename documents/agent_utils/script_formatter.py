def format_podcast_script(script_data):
    """
    Format podcast script data into a readable format with speaker labels.
    
    Args:
        script_data (list): List of dictionaries containing speaker and text information
        
    Returns:
        str: Formatted script with speaker labels
    """
    formatted_script = "Read aloud in a warm, welcoming tone\n\n"
    
    for entry in script_data:
        speaker = entry['speaker']
        text = entry['text']
        formatted_script += f"{speaker}: {text}\n"
    
    return formatted_script


if __name__ == "__main__":
    script_data = [{'speaker': 'Speaker 1',
  'text': "Welcome back to BookCast! Today, we're kicking off a deep dive into “Act Like a Success, Think Like a Success.” This book is just gold."},
 {'speaker': 'Speaker 2',
  'text': "I'm all ready! This book is ready for success! What a great time in history to unleash all this content!"},
 {'speaker': 'Speaker 1',
  'text': 'Exactly! First, he dedicates it to his mother, father, and wife; those most instrumental to helping him rise. Faith, Hard Work and Inspiration.'},
 {'speaker': 'Speaker 2',
  'text': 'Family. You cant fake those close to you. Isnt that what is needed for his vision, success? What a set up!!!'},
 {'speaker': 'Speaker 1',
  'text': 'He continues this, as your gift is calling…and that he feels being flown to perform just flooded him over. "Was told I would never amount to anything", he states.'},
 {'speaker': 'Speaker 2',
  'text': 'Thats heavy though to think those thoughts in action over the world performing. And that his family is all he wants!" I really want you, good health, Financial freedom"!!!! WOW he really wants all, not partially.'},
 {'speaker': 'Speaker 1',
  'text': 'Really lets the audience know with spending to get book that means we’re ready for success, no more time wasted!!!'},
 {'speaker': 'Speaker 2',
  'text': 'No one skips and skims here! We are ready for full deep and true focus on being aligned for all!!!'},
 {'speaker': 'Speaker 1',
  'text': 'Yeah it’s for retiree’s, young folk, fresh folk, ALL THE FOLK!!!!!! The words want people that say enough. Those that say THIS IS IT!!!!! This cant be what all I am built for!!!'},
 {'speaker': 'Speaker 2',
  'text': 'That can lead to getting everything, by reclaiming and realigning yourself in truth!'},
 {'speaker': 'Speaker 1',
  'text': 'That people know in them already have it!!!'},
 {'speaker': 'Speaker 2',
  'text': 'Its about the riches in all. Universe gives when its done out of gifts'},
 {'speaker': 'Speaker 1',
  'text': 'Incorporating that new flavor with community, relationships!'},
 {'speaker': 'Speaker 2',
  'text': 'Yes I never really know, to use my skills now with what God gave!!! This will allow people, to learn how I have the drive, all together to feel fulfilled in wealth!!'},
 {'speaker': 'Speaker 1',
  'text': 'His journey can give what needs for that self that has been not allowed with just one. That’s his gift, the art of success comes by knowing himself to take us with, into the riches life offers! "Act Like...Think Like"."'},
 {'speaker': 'Speaker 2',
  'text': 'Okay I’m at the chapter names to see his vision, there is one chapter you were going to dig into chapter 1.'},
 {'speaker': 'Speaker 1', 'text': 'Absolutely! Chapter 1 '},
 {'speaker': 'Speaker 2', 'text': 'Yeah how do you handle. I'},
 {'speaker': 'Speaker 1',
  'text': 'Being ready in reality? Releasing your inner lids, its TIME! You stop limiting what has been taught. Its our abilities. When the opinion of someone stops, and steals the opportunity!!'},
 {'speaker': 'Speaker 2',
  'text': 'And that starts from a little old kid, and the parents dont listen or hold them higher….!!!! I do feel thats our new day and now! We arent limited, for we have the gift.'},
 {'speaker': 'Speaker 1',
  'text': 'Whats our sign if our inner lid is on in a sense? How we think! I want freedom in waking up with excitement, if your busy, always have space then you can take that mask!'},
 {'speaker': 'Speaker 2',
  'text': 'Then its freedom that leads freedom!!!!! It must to begin with YOU though!!!'},
 {'speaker': 'Speaker 1',
  'text': 'Yes freedom to build into promises. Our lack comes because it seems more right then wrong!!!!! That we are afraid when others fail on our path is another thing. That taking is just for us but never.!'},
 {'speaker': 'Speaker 2',
  'text': 'Yeah its also something our mind, like we were trained to be blind all this time! What is most heavy to our journey when its not our desire. That needs time.'},
 {'speaker': 'Speaker 1',
  'text': 'Thats what he said. Because nobody does understand the need for you as the reason you would be great with. That there in is YOU!!'},
 {'speaker': 'Speaker 2',
  'text': 'Right yeah I find some heavy thoughts like fear from what one would describe your success, then how it really has, and does for your vision!!! WOW!!! You just took so far as knowing!'},
 {'speaker': 'Speaker 1',
  'text': 'It could go like that! But you cant get rid of them ever with their experiences unless. He looks at in prison with a mindset of looking to find that prison has changed! There a freedom with every human and thought to come if to them.'},
 {'speaker': 'Speaker 2',
  'text': 'Just be positive with everything that breaks!! But let opportunity become the biggest decision to lead where to make those days!!!'},
 {'speaker': 'Speaker 1',
  'text': 'Thats hard when there is fear all those times that lead you too this!!!! The hardest thing though is to quit or not?!!! Now your on!!!!'},
 {'speaker': 'Speaker 2',
  'text': 'Or that we all need to think that not following can be our victory!'},
 {'speaker': 'Speaker 1',
  'text': 'He makes us look out what people make good with others but with few others!!!!!! Yes that one can use so better with family in service of our life.'},
 {'speaker': 'Speaker 2',
  'text': 'That with us is always one point. That this what put you high for life. And that all, will give much because this will always build our win!! WOW! that this action leads to unlock!'},
 {'speaker': 'Speaker 1',
  'text': 'It has lead him all way through comedy!! He now leads us with your that must not, cannot make, or feel and that our feelings need nothing else in us that not with!!!! Talent what gives people to perform!!! Those give you!! To know about make and what gifts always needs!!!'},
 {'speaker': 'Speaker 2',
  'text': "In short Steve's, one gift that those, what there for for you??? Because what all. We must look it needs with what they've!!!! To find a new needs so do!! What the vision needs to follow with, but not need it all! That to do!!"},
 {'speaker': 'Speaker 1',
  'text': 'Yeah!!! 3, that other what gift??, when they??? How do???'},
 {'speaker': 'Speaker 2',
  'text': 'That comes easy???? WOW!!!! what gifts comes?? In needs, to now you. Its is new that. The that need today!! Because to a know this all! That one the that??? How!!!! And that from and today but that? What for needs.'},
 {'speaker': 'Speaker 1',
  'text': 'Steve has had so!!! To had need to. The what and it does is with!!!!! Those in!!! Or just you to??? WOW That, new the be. This that make just be, it!! Those get you!'},
 {'speaker': 'Speaker 2',
  'text': 'The not does not for those it!!!! Need on needs of. Find what to It!!!!! The who??? That for needs. Does your???? Just in on needs. We from of the one is'},
 {'speaker': 'Speaker 1', 'text': 'I was in The of?? and!!!!'},
 {'speaker': 'Speaker 2',
  'text': 'Yeah now??? We not get get make is We one to!! All in??? It'},
 {'speaker': 'Speaker 1',
  'text': 'He needs then all those and!!!!!! You The the does, of to for in.. does in??'},
 {'speaker': 'Speaker 2',
  'text': 'Now that get use to what all!!!!! Those You. to????? In get make??.. Is it? that is'},
 {'speaker': 'Speaker 1',
  'text': 'He those you You new, those!!! that you it, fun with!!! to need? focus??? and new '},
 {'speaker': 'Speaker 2',
  'text': 'Today, there we is a? Those we. now or all we be! or today???? In???'},
 {'speaker': 'Speaker 1',
  'text': 'Definitely, we there we can. One can what has It focus, or focus be?? you those with we.'},
 {'speaker': 'Speaker 2',
  'text': 'We now!!, we on all and we does? to does not, to? In We the can'}]
    formatted_script = format_podcast_script(script_data)
    print(formatted_script)
