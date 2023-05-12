import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
most_viewed_add_platform = ad_clicks.groupby(['utm_source'])['user_id'].count().reset_index()
print(most_viewed_add_platform)
print(most_viewed_add_platform.max())
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull().apply(lambda x : False if x == True else True)
print(ad_clicks.head(10))
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
print(clicks_by_source)
clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()
print(clicks_pivot)
clicks_pivot['percent_clicked'] = \
   (clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False]))*100
print(clicks_pivot)
same_adA_AdB = ad_clicks.groupby(['experimental_group'])['user_id'].count().reset_index()
print(same_adA_AdB)
greater_percentage_clicked = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
print(greater_percentage_clicked)
greater_percentage_clicked_pivot = greater_percentage_clicked.pivot(index = 'experimental_group', columns = 'is_click'\
                                                                    , \
                                                                   values = 'user_id')
print(greater_percentage_clicked_pivot)
greater_percentage_clicked_pivot['comparison_percent_A_B'] = \
    (greater_percentage_clicked_pivot[True]/ \
    (greater_percentage_clicked_pivot[True]+
    greater_percentage_clicked_pivot[False]))*100
print(greater_percentage_clicked_pivot)
#looks like the ad used in comparison a wins percent wise
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks.head())
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(b_clicks.head)
click_by_day_A = a_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()
click_by_day_A_pivot = click_by_day_A.pivot(index = 'day', columns = 'is_click', values = 'user_id')
click_by_day_A_pivot['percent_comparison'] = \
    (click_by_day_A_pivot[True]/ \
    (click_by_day_A_pivot[True]+\
    click_by_day_A_pivot[False]))*100
print(click_by_day_A_pivot)
click_by_day_B = b_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()
click_by_day_B_pivot = click_by_day_B.pivot(index = 'day', columns = 'is_click', values = 'user_id')
click_by_day_B_pivot['percent_comparison'] = \
    (click_by_day_B_pivot[True]/ \
    (click_by_day_B_pivot[True]+\
    click_by_day_B_pivot[False]))*100
print(click_by_day_B_pivot)
#recommend Ad A