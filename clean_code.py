###### Bod Code #######

s = [88, 92, 79, 93, 85]   # student test scores
print(sum(s) / len(s))     # print mean of test scores


# curve scores with square root method and store in new list
s1 = [x ** 0.5 * 10 for x in s]
print(sum(s1) / len(s1))


####### Better Code ########

import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))


###### Other Examples #########

age_list = [47, 12, 28, 52, 35]
for i, age in enumerate(age_list):
	if age < 18:
		is_minor = True
		age_list[i] = "minor"


###### Giving Good Names #######

# bad

def count_unique_values_of_names_list_of_set(names_list):
	return len(set(names_list))

# better


def count_unique_values(arr):
	return len(set(arr))


###### When you see this code below ########

def plot_active_users(client, start_date, end_date, bin):
	"""Plots number of active users per bin unit between start_date(inclusive) and end_date (exclusive)."""
	date_format = get_date_format(bin)
	dev_team = [ObjectId(user) for user in pd.read_csv('dev.csv')['id']]
	users = [record['_id'] for record in client.xyz.users.find({'_id'}: {'$nin': dev_team}, {})]
	results = client.xyz.actions.aggregate([
				{'$match': {'timestamp': {'$gte': start_date, '$lt': end_date}, 'actor': {'$in': users}}}, {"$project": {"date":
				{"$group": {"_id": "$date", "activeUsers": {"$addToSet": "$actor"}, }}, {"$sort": {"_id": 1}}])

	dates, labels = date_range(start_date, end_date, date_format, bin)
	activeUsers = np.zeros(len(dates))
	for record in results:
		num_active_users = len(record['activeUsers'])
		date = record['_id']
		i = dates.index(date)
		activeUsers[i] = num_active_users
	create_plot(labels, activeUsers, 'Active Users Per ' + bin.title(),
	            bin.title(), 'Number of Active Users', 'active_user')
	return labels, active_users


####### With some arrangements #########

def plot_active_users(client, start_date, end_date, bin):
	"""Plots number of active users per bin unit between start_date
	(inclusive) and end_date (exclusive)."""

	date_format = get_date_format(bin)
	dev_team = [ObjectId(user) for user in pd.read_csv('dev.csv')['id']]
	users = client.xyz.users.find({'_id': {'$nin': dev_team}}, {})
	users = [record['_id'] for record in users]

	results = client.xyz.actions.aggregate([
		{'$match': {
			'timestamp': {'$gte': start_date, '$lt': end_date},
			'actor': {'$in': users}
		}},
		{"$project": {
			"date": {
				"$dateToString": {
					"format": date_format,
					"date": "$timestamp"
			}},
			{"$group": {
				"_id": "$date",
				"activeUsers": {"$addToSet": "$actor"},
			}},
			{"$sort": {
				"_id": 1
			}}
	])

	dates, labels = date_range(start_date, end_date, date_format, bin)
	activeUsers = np.zeros(len(dates))

	for record in results:
		num_active_users = len(record['activeUsers'])
		date = record['_id']
		i = dates.index(date)
		activeUsers[i] = num_active_users

	title = 'Active Users Per ' + bin.title()
	filename = 'active_users_per_{}.png'.format(bin)
	x_label = bin.title()
	y_label = 'Number of Active Users'

	create_plot(labels, active_users, title, x_label, y_label, filename)

	return labels, active_users
