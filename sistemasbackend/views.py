from django.http import HttpResponse

from base.models import Directory

def about(request):
    # dirRoot= Directory.objects.get(pk=1)
    response= test()
    print(response)
    return HttpResponse(response)

def path_to_root_directory(directory_id):
    if directory_id is None:
        return []
    directory = Directory.objects.get(pk=directory_id)
    print("ID",directory.id)
    result = []
    if directory.belongs_to:
        print("DIRECTORIO CTMRE", directory.belongs_to.id)
        result = path_to_root_directory(directory.belongs_to.id)
        result.append(directory)
    return result

def test():
    query= '''
    select  id,
            name, belongs_to_id, 
    from    base_directory
    where   id like '31/%';
    '''
    return Directory.objects.raw(query)


def path_to_root_category(category_id):
    query = '''
    WITH RECURSIVE parents AS (
        SELECT base_directory.*, 0 AS relative_depth
        FROM base_directory
        WHERE id = %s

        UNION ALL

        SELECT base_directory.*, parents.relative_depth - 1
        FROM base_directory,parents
        WHERE base_directory.id = parents.belongs_to.id
    )
    SELECT id, name, belongs_to, relative_depth
    FROM parents
    ORDER BY relative_depth;
    '''
    return Directory.objects.raw(query, [category_id])