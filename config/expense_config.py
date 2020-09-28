expense_config = {
  'recurring': {
    'daily': [{
      'description': 'DESCRIPTION',
      'cost': 2.0
    }],
    'weekly': [{
      'description': 'DESCRIPTION',
      'day_of_week': [1, 4],
      'cost': 40.0
    }],
    'biweekly': [{
      'description': 'DESCRIPTION',
      'days_of_month': [5, 20],
      'cost': 40.0
    }],
    'monthly': [{
      'description': 'DESCRIPTION',
      'day_of_month': 20,
      'cost': 40.0
    }],
    'quarterly': [{
      'description': 'DESCRIPTION',
      'day_of_month': 1,
      'month_of_quarter': 2,
      'cost': 80,
    }],
    'yearly': [{
      'description': 'DESCRIPTION',
      'day_of_month': 15,
      'month_of_year': 10,
      'cost': 100,
    }],
  },
  'non_recurring': {
    'example_key': {
      'description': 'DESCRIPTION',
      'dates': [
        '2020-09-21'
      ],
      'cost': 125.0
    }
  }
}