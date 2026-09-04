from fairmat_network_projects.schema_packages.schema_package import (
    Engagement,
    NetworkProject,
    ResearchData,
    RDMStatus,
    Subproject,
)


def test_schema_package():
    project = NetworkProject(
        short_name='NetProj',
        rdm_landscape=RDMStatus(research_data=[ResearchData(volume='10-100 GB')]),
        engagement=[
            Engagement(
                title='Kickoff',
                start_date='2026-03-10',
                end_date='2026-03-10',
                activity_type='Meeting',
                notes='Kickoff meeting',
            )
        ],
    )

    assert project.short_name == 'NetProj'
    assert project.rdm_landscape.research_data[0].volume == '10-100 GB'
    assert len(project.engagement) == 1

    assert Subproject.data_driven_ai_based.label == 'data-driven / AI-based subproject'
    assert Subproject.Additional_info.label == 'Additional information'
