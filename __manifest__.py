
{
    'name': "Sample Theme",
    'summary': """
        sample page is here""",
    'description': """
        Long description of module's purpose
    """,
    'author': " My Company",
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",
    'category': "Theme",
    'version': "0.1",
    'depends': [
        'website',
        'base_setup',
        'mail',
        'resource',
        'web',
    ],
    'data': [
        'views/home.xml',
        'views/institution/institution.xml',
        'views/institution/about.xml',
        'views/institution/vision.xml',
        'data/website_data.xml',
        'views/institution/history.xml',
        'views/institution/rules.xml',
        'views/institution/emblem.xml',
        'views/institution/principal.xml',
        'views/institution/code.xml',
        'views/institution/fprincipals.xml',
        'views/institution/management.xml',
        'views/institution/pta.xml',
        'views/institution/adstaff.xml',
        'views/institution/scouncil.xml',
        'views/institution/rti.xml',
        'views/institution/organization.xml',
        'views/institution/sister-institution.xml',
        
        'views/department/department.xml',
        'views/department/english.xml',
        'views/department/commerce.xml',
        'views/department/economics.xml',
        'views/department/microbiology.xml',
        'views/department/biochemistry.xml',
        'views/department/computer-science.xml',
        'views/department/biotechnology.xml',
        'views/department/business-administration.xml',
        'views/department/mathematics.xml',
        'views/department/west-asian-studies.xml',
        'views/department/logistic.xml',
        'views/department/accounting.xml',

        'views/academics/academics.xml',
        'views/academics/programmes.xml',
        'views/academics/ug-admission.xml',
        'views/academics/pg-admission.xml',
        'views/academics/certificate.xml',
        'views/academics/learning.xml',
        'views/academics/calendar.xml',
        'views/academics/human-values.xml',

        'views/students zone/students-zone.xml',
        'views/students zone/nss.xml',
        'views/students zone/ncc.xml',






    ],
    'assets': {
        'web.assets_frontend': [
            '/sample_theme/static/css/vision.css',

        ],

    }
}
