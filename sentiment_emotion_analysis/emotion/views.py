from django.shortcuts import render, redirect, HttpResponse
from .forms import Emotion_Typed_Tweet_analyse_form, Emotion_Imported_Tweet_analyse_form
from .emotion_analysis_code import emotion_analysis_code
from .tweepy_emotion import Import_tweet_emotion

def emotion_analysis(request):
    return render(request, 'home/emotion.html')

def emotion_analysis_type(request):
    if request.method == 'POST':
        form = Emotion_Typed_Tweet_analyse_form(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['emotion_typed_tweet']
            try:
                analyse = emotion_analysis_code()
                emotion = analyse.predict_emotion(tweet)
                context = {'tweet': tweet, 'emotion': emotion}
                return render(request, 'home/emotion_type_result.html', context)
            except Exception as e:
                # Handle the exception if the analysis fails
                return HttpResponse(f"Error: {str(e)}")
        else:
            # If the form is not valid, render the form again with errors
            return render(request, 'home/emotion_type.html', {'form': form})
    else:
        form = Emotion_Typed_Tweet_analyse_form()
        return render(request, 'home/emotion_type.html', {'form': form})

def emotion_analysis_import(request):
    if request.method == 'POST':
        form = Emotion_Imported_Tweet_analyse_form(request.POST)
        if form.is_valid():
            handle = form.cleaned_data['emotion_imported_tweet']
            tweet_text = Import_tweet_emotion()
            analyse = emotion_analysis_code()
            try:
                if handle.startswith('#'):
                    list_of_tweets = tweet_text.get_hashtag(handle)
                else:
                    list_of_tweets = tweet_text.get_tweets(handle)
                    if not handle.startswith('@'):
                        handle = '@' + handle
                
                list_of_tweets_and_emotions = [(tweet, analyse.predict_emotion(tweet)) for tweet in list_of_tweets]
                
                context = {
                    'list_of_tweets_and_emotions': list_of_tweets_and_emotions,
                    'handle': handle
                }
                
                if handle.startswith('#'):
                    return render(request, 'home/emotion_import_result_hashtag.html', context)
                else:
                    return render(request, 'home/emotion_import_result.html', context)
            except Exception as e:
                # Handle the exception if the import or analysis fails
                return HttpResponse(f"Error: {str(e)}")
        else:
            # If the form is not valid, render the form again with errors
            return render(request, 'home/emotion_import.html', {'form': form})
    else:
        form = Emotion_Imported_Tweet_analyse_form()
        return render(request, 'home/emotion_import.html', {'form': form})
