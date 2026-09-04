from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
    Datetime,
    MEnum,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

configuration = config.get_plugin_entry_point(
    'fairmat_network_projects.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()

try:
    from fairmat_members.schema_packages.schema_package import (
        Person as FAIRmatMemberPerson,
    )
except Exception:  # pragma: no cover - optional cross-plugin dependency
    FAIRmatMemberPerson = None


PROJECT_TYPE = MEnum(
    'Collaborative Research Center',
    'Cluster of Excellence',
    'Research Unit',
    'Research Training Group',
    'EU Project',
    'International Project',
    'Industry',
    'Other',
)

AREAS_OF_INTEREST = MEnum(
    'Set up and operate a NOMAD Oasis for the project',
    'Publish project data in NOMAD Central',
    'Develop electronic lab notebooks for specific experiments and workflows',
    'Connect laboratory instruments to NOMAD for automated data transfer',
    'Develop parsers for project-specific data formats',
    'Develop project-specific NOMAD schemas and metadata models',
    'Develop search and exploration tools for project research data',
    'Develop data analysis and visualization tools',
    'Automate data processing and analysis workflows',
    'Integrate computational workflows and simulation data with NOMAD',
    'Integrate NOMAD with existing project data infrastructure and services',
    'Enable data sharing between project researchers and subprojects',
    'Set up workflows for publishing FAIR datasets',
    'Connect datasets with publications and persistent identifiers',
    'Establish common RDM workflows across project subprojects',
    'Develop data management plans and RDM guidelines for the project',
    'Train project researchers to use NOMAD and FAIR RDM practices',
    'Provide hands-on support for adopting NOMAD in individual subprojects',
)

ACTIVITY_TYPE = MEnum(
    'Meeting',
    'Seminar',
    'Tutorial',
    'Workshop',
    'Other',
)

RESEARCH_MODE = MEnum(
    'Experimental only',
    'Computational only',
    'Experimental and computational',
)


class Person(ArchiveSection):
    m_def = Section(label_quantity='name')

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    email = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )


class Contact(ArchiveSection):
    m_def = Section(label_quantity='name')

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    email = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    role = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )


class Organization(ArchiveSection):
    m_def = Section(label_quantity='name')

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    short_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    webpage = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
    )


class Subproject(ArchiveSection):
    m_def = Section(label_quantity='Sub Projects')

    title = Quantity(
        type=str,
        label='subproject title',
        description='Provide the title of the subproject.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    project_heads = Quantity(
        type=str,
        shape=['*'],
        label='project heads',
        description='List the names of the project heads.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    description = Quantity(
        type=str,
        label='sub project description',
        description='Provide a brief description of the subproject, including its objectives and scope.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )
    research_mode = Quantity(
        type=RESEARCH_MODE,
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    data_driven_ai_based = Quantity(
        type=bool,
        label='data-driven / AI-based subproject',
        description='Indicate whether the subproject is primarily data-driven or AI-based.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    Additional_info = Quantity(
        type=str,
        label='Additional information',
        description='Provide any additional information about the subproject.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

class ResearchLandscape(ArchiveSection):
    m_def = Section(label='Research Landscape')

    research_topics = Quantity(
        type=str,
        shape=['*'],
        label='main research topics',
        description='List the main scientific topics or themes of the project '
        '(e.g., catalysis, quantum materials, energy storage, photovoltaics). '
        'Add one topic per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    material_systems = Quantity(
        type=str,
        shape=['*'],
        label='main material systems studied',
        description='List the material systems the project works on. This can include broad categories '
        '(e.g., polymers, 2D materials) or specific materials (e.g., MoS2, Si, GaAs). '
        'Add one material system per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    research_methods = Quantity(
        type=str,
        shape=['*'],
        label='main methods and techniques used',
        description='List the main experimental, computational, or analytical techniques used in the project '
        '(e.g., DFT, molecular dynamics, XRD, spectroscopy, microscopy). '
        'Add one technique per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    focus_description = Quantity(
        type=str,
        label='Project focus and scientific challenges',
        description='Describe the project\'s research focus and the main scientific problems or challenges '
        'it aims to address, and the general approach it takes.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )
    subprojects = SubSection(section_def=Subproject, repeats=True)


class ResearchData(ArchiveSection):
    m_def = Section(label='Research Data')

    name = Quantity(
        type=str,
        label='name of data entry',
        description='Provide a short descriptive name for this data entry to distinguish it from others.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    data_type = Quantity(
        type=MEnum(
            'DFT calculations',
            'Molecular dynamics simulations',
            'Spectroscopy data',
            'Microscopy data',
            'Device measurements',
            'Other',
        ),
        label='main type of research data',
        description='Select the type of data that best describes this entry.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    data_type_other = Quantity(
        type=str,
        label='other data type (please specify)',
        description='If you selected "Other", provide a short description.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    file_format = Quantity(
        type=str,
        shape=['*'],
        label='file formats',
        description='List the file formats used for this data type. Add one format per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    volume = Quantity(
        type=str,
        label='typical dataset sizes and volume',
        description='Provide typical dataset sizes or estimated data volumes (e.g., 10-100 GB, 1 TB/year).',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    software_instruments = Quantity(
        type=str,
        shape=['*'],
        label='software or instruments used to collect/generate the data',
        description='List software and instruments used for this data type. Add one item per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )


class RDMStatus(ArchiveSection):
    m_def = Section(label='RDM Landscape')

    data_storage = Quantity(
        type=MEnum(
            '1- Local servers',
            '2- HPC storage',
            '3- Cloud, e.g., AWS, institutional Cloud, Google Cloud, dropbox',
            '4- External repositories, e.g., Zenodo, NOMAD, institutional repositories',
            '5- Other',
        ),
        shape=['*'],
        label='how is research data currently stored?',
        description='Select all options that apply to the project\'s current data storage practices. '
        'For "Other", please specify the storage solution in the next field.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    data_storage_other = Quantity(
        type=str,
        label='other storage solution (please specify)',
        description='If you selected "Other", please specify the storage solution used '
        '(e.g., custom infrastructure, partner systems).',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    metadata_documentation = Quantity(
        type=MEnum(
            '1- Lab notebooks',
            '2- Electronic lab notebooks',
            '3- Scripts / workflow managers',
            '4- Spreadsheets',
            '5- Catalogues',
            '6- Other',
        ),
        shape=['*'],
        label='how is metadata documented?',
        description='Select all options that apply to how the project documents metadata and experimental/computational details. ',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    metadata_documentation_other = Quantity(
        type=str,
        label='other metadata documentation method (please specify)',
        description='If you selected "Other", please specify how metadata is documented '
        '(e.g., custom databases, LIMS, internal tools).',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    publication_and_archiving = Quantity(
        type=str,
        shape=['*'],
        label='where is data ultimately published or archived?',
        description='List the repositories, journals, or platforms where data is published or archived. Add one item per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    existing_data_management_tools = Quantity(
        type=str,
        shape=['*'],
        label='are there existing data management tools used in your project?',
        description='List any data management tools, platforms, or software used in your project '
        '(e.g., electronic lab notebooks, databases, workflow managers, data catalogues, internal systems). '
        'Provide names and brief details if relevant.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    existing_standards = Quantity(
        type=str,
        shape=['*'],
        label='are there existing standards or schemas used in your project?',
        description='List any standards, ontologies, or metadata schemas used in your project '
        '(e.g., NeXus, CIF, JSON schemas, domain-specific standards). '
        'Provide names and brief details if relevant.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    policies_and_guidelines = Quantity(
        type=str,
        label='Are there established rules and internal policy in the project regarding RDM?',
        description='Describe any internal policies, guidelines, or best practices regarding research data management within the project. Provide links if available.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    data_flows = Quantity(
        type=str,
        label='Describe any recurring data flows between particular subprojects?',
        description='Describe any recurring data flows between particular subprojects, including the types of data exchanged and the frequency of exchange.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )


    research_data = SubSection(
        section_def=ResearchData,
        repeats=True,
    )


class NomadInterests(ArchiveSection):
    m_def = Section(label='Potential FAIRmat/NOMAD Support')

    areas_of_interest = Quantity(
        type=AREAS_OF_INTEREST,
        shape=['*'],
        label='which of the following areas would be interesting for the project?',
        description=(
            'Select all topics where support, integration, or collaboration with '
            'FAIRmat and NOMAD would be most beneficial for your project.'
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    additional_areas_of_interest = Quantity(
        type=str,
        shape=['*'],
        label='other areas of interest (free text)',
        description='Add additional topics that are not covered by the controlled list.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )


class Engagement(ArchiveSection):
    m_def = Section(label='Engagement')

    title = Quantity(
        type=str,
        label='Title',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    start_date = Quantity(
        type=Datetime,
        label='Start date',
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
    )

    end_date = Quantity(
        type=Datetime,
        label='End date',
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
    )

    activity_type = Quantity(
        type=ACTIVITY_TYPE,
        label='Type',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    notes = Quantity(
        type=str,
        label='Notes',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )
    #TODO : Add a field that can reference to events from the event database

class NetworkProject(Schema):
    m_def = Section(
        label='Network Project',
        categories=[UseCaseElnCategory],
    )

    # General information (top-level so fields appear immediately in the entry form)
    code = Quantity(
        type=str,
        label='project code',
        description='The unique code assigned to the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    short_name = Quantity(
        type=str,
        label='short name',
        description='A short name or acronym for the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    complete_name = Quantity(
        type=str,
        label='complete name',
        description='The full official name of the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    project_type = Quantity(
        type=PROJECT_TYPE,
        label='project type',
        description='Select the type of project from the predefined list.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    has_inf_project = Quantity(
        type=bool,
        label='Has INF project',
        description='Indicate whether and INF project is part of the network project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    gepris_url = Quantity(
        type=str,
        label='Funders URL',
        description='Provide the URL to the project\'s page on the funder\'s website (e.g., DFG GEPRIS).',
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
    )
    webpage = Quantity(
        type=str,
        label='Project webpage',
        description='Provide the URL to the project\'s official webpage.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
    )
    start_date = Quantity(
            type=Datetime,
            label='start date',
            description='Provide the start date of the project.',
            a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
    )
    end_date = Quantity(
        type=Datetime,
        label='end date',
        description='Provide the end date of the current funding period of the project.', 
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateEditQuantity),
    )
    current_funding_phase = Quantity(
        type=int,
        label='current funding phase',
        description='Provide the current funding phase of the project, e.g., 1 for the first phase, 2 for the second phase, etc.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    spokesperson = Quantity(
        type=str,
        shape=['*'],
        label='spokesperson(s)',
        description='List the spokesperson(s) of the project. Add one name per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    contact_person = Quantity(
        type=str,
        label='contact person for research data management',
        description='Provide the name of the person responsible for research data management in the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    role_of_contact_person = Quantity(
        type=str,
        label='role of contact person',
        description='Provide the role or position of the contact person within the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    email_of_contact_person = Quantity(
        type=str,
        label='email of contact person',
        description='Provide the email address of the contact person responsible for research data management.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    applicant_institutes = Quantity(
        type=str,
        shape=['*'],
        label='applicant institutes',
        description='List the institutes that are applicants in the project. Add one institute per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    participating_institutes = Quantity(
    type=str,
    shape=['*'],
    label='participating institutes',
    description='List the institutes that are participating in the project. Add one institute per line.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    number_of_pis = Quantity(
        type=int,
        label='number of principal investigators',
        description='Provide the number of principal investigators in the project.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )    
    number_of_researchers = Quantity(
        type=int,
        label='number of researchers',
        description='Provide the number of researchers in the project, including postdocs, graduate students, and other research staff.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    number_of_data_stewards = Quantity(
        type=int,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    # TODO: link to FAIRmat members plugin for PIs to directly create references.
    involved_fairmat_pis = Quantity(
        type=str,
        shape=['*'],
        label='involved FAIRmat PIs',
        description='List the FAIRmat principal investigators involved in the project. Add one name per line.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_landscape = SubSection(section_def=ResearchLandscape)
    rdm_landscape = SubSection(section_def=RDMStatus)
    nomad_interests = SubSection(section_def=NomadInterests)
    engagement = SubSection(section_def=Engagement, repeats=True)


m_package.__init_metainfo__()
