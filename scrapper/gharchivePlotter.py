import matplotlib.pyplot as plt
import numpy as np

jsonarray = [
  {
    'CreateEvent': 183775,
    'IssueCommentEvent': 99271,
    'WatchEvent': 107234,
    'PullRequestReviewCommentEvent': 27644,
    'PushEvent': 761788,
    'PullRequestEvent': 84235,
    'CommitCommentEvent': 2770,
    'MemberEvent': 5369,
    'ReleaseEvent': 5413,
    'ForkEvent': 35664,
    'DeleteEvent': 33156,
    'IssuesEvent': 50523,
    'PublicEvent': 1484,
    'GollumEvent': 7102
  },
  {
    'CreateEvent': 310984,
    'IssueCommentEvent': 150722,
    'WatchEvent': 176547,
    'PullRequestReviewCommentEvent': 37706,
    'PushEvent': 1303531,
    'PullRequestEvent': 129803,
    'CommitCommentEvent': 4365,
    'MemberEvent': 8463,
    'ReleaseEvent': 8428,
    'ForkEvent': 58562,
    'DeleteEvent': 52687,
    'IssuesEvent': 80067,
    'PublicEvent': 2366,
    'GollumEvent': 11854
  },
  {
    'CreateEvent': 437148,
    'IssueCommentEvent': 196127,
    'WatchEvent': 244212,
    'PullRequestReviewCommentEvent': 47239,
    'PushEvent': 1869414,
    'PullRequestEvent': 171968,
    'CommitCommentEvent': 5880,
    'MemberEvent': 11424,
    'ReleaseEvent': 11803,
    'ForkEvent': 81297,
    'DeleteEvent': 70718,
    'IssuesEvent': 107993,
    'PublicEvent': 3431,
    'GollumEvent': 16904
  },
  {
    'CreateEvent': 639295,
    'IssueCommentEvent': 302595,
    'WatchEvent': 360599,
    'PullRequestReviewCommentEvent': 77649,
    'PushEvent': 2670194,
    'PullRequestEvent': 259700,
    'CommitCommentEvent': 8745,
    'MemberEvent': 17825,
    'ReleaseEvent': 17192,
    'ForkEvent': 121551,
    'DeleteEvent': 104810,
    'IssuesEvent': 159036,
    'PublicEvent': 5238,
    'GollumEvent': 24160
  },
  {
    'CreateEvent': 852437,
    'IssueCommentEvent': 417540,
    'WatchEvent': 483807,
    'PullRequestReviewCommentEvent': 110372,
    'PushEvent': 3487668,
    'PullRequestEvent': 351994,
    'CommitCommentEvent': 11764,
    'MemberEvent': 24625,
    'ReleaseEvent': 23216,
    'ForkEvent': 164504,
    'DeleteEvent': 140589,
    'IssuesEvent': 213246,
    'PublicEvent': 7147,
    'GollumEvent': 33401
  },
  {
    'CreateEvent': 1064325,
    'IssueCommentEvent': 527918,
    'WatchEvent': 607970,
    'PullRequestReviewCommentEvent': 141968,
    'PushEvent': 4299559,
    'PullRequestEvent': 443985,
    'CommitCommentEvent': 14675,
    'MemberEvent': 31439,
    'ReleaseEvent': 29047,
    'ForkEvent': 207863,
    'DeleteEvent': 176075,
    'IssuesEvent': 266434,
    'PublicEvent': 8839,
    'GollumEvent': 40986
  },
  {
    'CreateEvent': 1268719,
    'IssueCommentEvent': 636282,
    'WatchEvent': 730109,
    'PullRequestReviewCommentEvent': 173084,
    'PushEvent': 5101383,
    'PullRequestEvent': 533779,
    'CommitCommentEvent': 17125,
    'MemberEvent': 37711,
    'ReleaseEvent': 34621,
    'ForkEvent': 248730,
    'DeleteEvent': 210699,
    'IssuesEvent': 318790,
    'PublicEvent': 10548,
    'GollumEvent': 49330
  }
]
for i in range(7):
    json = jsonarray[i]
    colors = ["firebrick", "red", "darksalmon", "gold", "olivedrab", "darkgreen", "lightseagreen", "navy", "m", "orangered", "lawngreen", "lightsteelblue", "dimgray", "lightgray"]
    labels = np.array(list(json.keys()))
    vals = np.array(list(json.values()))
    percentages = 100.*vals/vals.sum()
    explode = [0.07]*len(vals)

    patches, texts = plt.pie(vals, colors=colors,explode=explode, startangle=90, radius=1.2)
    legendlabels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, percentages)]
    plt.legend(patches, legendlabels, loc='best', bbox_to_anchor=(1., 0.4),
               fontsize=8)
    plt.subplots_adjust(right=0.5)
    plt.title("0%d-06-2018" % (i+1))
    plt.show()