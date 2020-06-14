import json
import requests

class backend_task:
    def __init__(self) -> None:
        self.URL = 'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'

    def get_json_data(self) -> dict:
        api = requests.get(self.URL)
        headers = api.headers
        if api.status_code == 200:
            return json.loads(api.text)
        else:
            return {}

    def date_suffix(self, date) -> str:
        formatted_date = str(date)
        if date == 1 or date == 21 or date == 31:
            formatted_date += 'st'
        elif date == 2 or date == 22:
            formatted_date += 'nd'
        elif date == 3 or date == 23:
            formatted_date += 'rd'
        else:
            formatted_date += 'th'
        return formatted_date

    def format_date(self, data) -> dict:
        month_dict = {
            'jan': 'January',
            'feb': 'February',
            'mar': 'March',
            'apr': 'April',
            'may': 'May',
            'jun': 'June',
            'jul': 'July',
            'aug': 'August',
            'sep': 'September',
            'oct': 'October',
            'nov': 'November',
            'dec': 'December',
        }
        month_num_dict = {
            'jan': '01',
            'feb': '02',
            'mar': '03',
            'apr': '04',
            'may': '05',
            'jun': '06',
            'jul': '07',
            'aug': '08',
            'sep': '09',
            'oct': '10',
            'nov': '11',
            'dec': '12',
        }

        # Format paid events list
        for i in range(len(data['paid'])):
            start_date = data['paid'][i].get('confStartDate', -1)
            end_date = data['paid'][i].get('confEndDate', -1)
            data['paid'][i]['sortDateValue'] = int(
                start_date[-4:]
                + month_num_dict.get(start_date[3:6].lower(), 0)
                + start_date[:2]
            )
            if start_date != -1:
                date = int(end_date[:2])
                month = end_date[3:6]
                year = end_date[-4:]
                formatted_date = self.date_suffix(date)
                formatted_month = month_dict.get(
                    month.lower(), month.lower().capitalize()
                )
                data['paid'][i]['confStartDate'] = (
                    formatted_month + ' ' + formatted_date + ', ' + year
                )
            if end_date != -1:
                date = int(end_date[:2])
                month = end_date[3:6]
                year = end_date[-4:]
                formatted_date = self.date_suffix(date)
                formatted_month = month_dict.get(
                    month.lower(), month.lower().capitalize()
                )
                data['paid'][i]['confEndDate'] = (
                    formatted_month + ' ' + formatted_date + ', ' + year
                )

        # Format free events list
        for i in range(len(data['free'])):
            start_date = data['free'][i].get('confStartDate', -1)
            end_date = data['free'][i].get('confEndDate', -1)
            data['free'][i]['sortDateValue'] = int(
                start_date[-4:]
                + month_num_dict.get(start_date[3:6].lower(), 0)
                + start_date[:2]
            )
            if start_date != -1:
                date = int(end_date[:2])
                month = end_date[3:6]
                year = end_date[-4:]
                formatted_date = self.date_suffix(date)
                formatted_month = month_dict.get(
                    month.lower(), month.lower().capitalize()
                )
                data['free'][i]['confStartDate'] = (
                    formatted_month + ' ' + formatted_date + ', ' + year
                )
            if end_date != -1:
                date = int(end_date[:2])
                month = end_date[3:6]
                year = end_date[-4:]
                formatted_date = self.date_suffix(date)
                formatted_month = month_dict.get(
                    month.lower(), month.lower().capitalize()
                )
                data['free'][i]['confEndDate'] = (
                    formatted_month + ' ' + formatted_date + ', ' + year
                )

        return data

    def merge_paid_and_free_confs(self, data) -> list:
        events = data['free']
        events.extend(data['paid'])

        return events

    def json_to_human_readable(self, data) -> list:
        f = open('human_readable_data.txt', 'w')
        human_readable_list = []
        for event in data:
            temp = []
            temp.append(event['confName'].strip())
            temp.append(event['confStartDate'].strip())
            temp.append(event['city'].strip())
            temp.append(event['state'].strip())
            temp.append(event['country'].strip())
            temp.append(event['entryType'].strip())
            temp.append(event['confUrl'].strip())
            f.write(', '.join(temp))
            f.write('\n')
            human_readable_list.append(temp)
        f.close()
        return human_readable_list

    def remove_exact_duplicate_confs(self, data) -> list:
        f = open('exact_duplicate_confs.txt', 'w')
        removed_duplicates_list = []
        for i in range(len(data) - 1):
            if data[i] in data[i + 1 :]:
                f.write(', '.join(data[i]))
                f.write('\n')
                removed_duplicates_list.append(data[i])
            else:
                pass
        f.close()

        return removed_duplicates_list


if __name__ == '__main__':
    api = backend_task()
    json_data = api.get_json_data()
    formatted_date = api.format_date(json_data)
    merged_conf_data = api.merge_paid_and_free_confs(formatted_date)
    json_to_human_readable = api.json_to_human_readable(merged_conf_data)
    remove_exact_duplicate_confs = api.remove_exact_duplicate_confs(json_to_human_readable)