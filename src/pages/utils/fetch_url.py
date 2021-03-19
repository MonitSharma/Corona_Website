# define the function fetch url, that'll go to
# the desired url and scrape the data from there


def fetch_url(date, country=None):
    """
    This function fetches the url of the recent reports
    :param date:
    :param country:
    :return:
    """

    DATA_URL = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                "csse_covid_19_daily_reports/{}.csv".format(date.date().strftime("%m-%d-%Y")))
    # now we know the US does not follow the conventional dd/mm/yyyy fromat
    # so we have to make a special case just for them
    if country == " US":
        DATA_URL = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                    "csse_covid_19_daily_reports_us/{}.csv".format(date.date().strftime("%m-%d-%Y")))

    return DATA_URL

