# Permissions name and code
archive_permission = ('_project_can_archive_permission', 'Can archive permission')
all_crud_permission = ('_project_can_do_all_crud_permission', 'Can do all crud')
view_only_permission = ('_project_can_view_only_permission', 'Can view only permission')
view_classified_information_permission = ('_project_can_view_classified_information',
'Can view classified information')
document_management_permission = ('_project_can_upload_or_delete_documents',
'Can upload or delete documents')
# Permission list associated with groups
super_group_permissions = [archive_permission, all_crud_permission, view_only_permission,
                           view_classified_information_permission,
                           document_management_permission]
document_management_group_permissions = [document_management_permission]
view_group_permission = [view_only_permission]
archive_group_permission = [archive_permission]
# Group names
PROJECT_SUPER_GROUP = '_project_super_group'
PROJECT_VIEW_ONLY_GROUP = '_project_view_only_group'
PROJECT_DOCUMENT_MANAGEMENT_GROUP = '_project_document_management_group'
PROJECT_ARCHIVE_GROUP = '_project_archive_group'
# Group and permission list mappings
project_permission_group = {PROJECT_SUPER_GROUP: super_group_permissions,
                            PROJECT_VIEW_ONLY_GROUP: view_group_permission,
                            PROJECT_DOCUMENT_MANAGEMENT_GROUP:
                                document_management_group_permissions,
                            PROJECT_ARCHIVE_GROUP: archive_group_permission}