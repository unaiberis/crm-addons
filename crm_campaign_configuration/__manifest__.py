# Copyright 2021 Berezi - Iker - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM campaign configuration",
    "version": "14.0.1.0.0",
    "author": "Avanzosc",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Sales/CRM",
    "depends": [
        "contacts",
        "crm",
        "utm",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/utm_source_views.xml",
        "views/utm_campaign_views.xml",
        "views/utm_medium_views.xml",
        "views/contact_medium_views.xml",
        "views/contact_source_views.xml",
        "views/contact_campaign_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
