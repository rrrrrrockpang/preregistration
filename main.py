import tea

tea.data("./df.csv", key="worker_id")

variables = [
    {
        'name': 'condition',
        'data type': 'nominal',
        'categories': ['SE', 'SD']
    },
    {
        'name': 'text_condition',
        'data type': 'nominal',
        'categories': ['show_both_stats', 'show_viz_stats_only']
    },
    {
        'name': 'wtp_final',
        'data type': 'interval'
    },
    {
        'name': 'superiority_special',
        'data type': 'ratio',
        'range': [0, 1]
    }
]

tea.define_variables(variables)

study_design = {
    'study_type': 'experiment',
    'independent variables': ['condition', 'text_condition'],
    'dependent variables': 'wtp_final'
}

tea.define_study_design(study_design)

tea.hypothesize(['condition', 'wtp_final'], ['condition: SE > SD'])

