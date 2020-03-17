import pandas as pd
from ticket import Ticket


def read_csv_as_dataframe(csv_path):
    return pd.read_csv(csv_path)


def clean_dataframe(df, columns2save):
    cols = list(df.columns)
    for column in cols:
        if column not in columns2save:
            df = df.drop(column, 1)
    return df


def create_dictionary_of_parameters(df, plan):
    df = clean_dataframe(df, list(plan.keys()))
    list_tickets = []
    for index, row in df.iterrows():
        single_ticket = Ticket()
        for key in plan:
            plan.get(key)(single_ticket, row[key])
        list_tickets.append(single_ticket)
    return list_tickets


def create_github_tickets(ticket_dict):
    for t in ticket_dict:
        t.create_github_issue()


def full_process(csv_path, plan):
    df = read_csv_as_dataframe(csv_path)
    ticket_dict = create_dictionary_of_parameters(df, plan)
    create_github_tickets(ticket_dict)


if __name__ == '__main__':
    csv_path = csv_to_plan_io_issues
    plan = {'Subject': Ticket.handle_title,
            'Description': Ticket.handle_description,
            'Type': Ticket.handle_type,
            'Assignee': Ticket.handle_assignee,
            'Sprint/Milestone': Ticket.handle_milestone,
            'Status': Ticket.handle_state,
            'Project': Ticket.handle_labels,
            '#': Ticket.handle_link}
    full_process(csv_path, plan)
