from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus

app_entry_point = AppEntryPoint(
    name='FAIRmatNetworkProjectsApp',
    description='Search and browse FAIRmat network projects.',
    app=App(
        label='FAIRmat Network Projects',
        path='fairmat-network-projects',
        category='FAIRmat',
        description='Search and browse FAIRmat network projects.',
        columns=Columns(
            selected=['entry_id'],
            options={
                'entry_id': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
            }
        ),
    ),
)
