
Plugin types
============
DataQualifer plugin              # logic for choosing how to process
ValueFormatter plugin       # formats value for writing
AttributeFormatter plugin   # formats an attribute for writing
ReferenceFormatter plugin   # formats the attribute reference (name, key or index)
WriteStream plugin          # writes formatted text


Trigger plugins
===============
Trigger(priority, no_passthrough
    , has_parent, has_child, is_native, is_class, is_instance, is_instanceof
    , is_subclassof, is_sequence, is_mapping, is_callable
    , has_attributes, has_properties, has_methods
    , is_type, is_numeric, is_boolean, is_float
    , type_matcher, parent_type_matcher, child_type_matcher
    , key_matcher, has_child_keys_matcher, has_length
    , has_min_length, has_max_length
    , has_min_attributes, has_max_attributes): returns True if handled else False to passthrough

Trigger#matches(value, parent, parent_reference): bool
Trigger#format(value, parent, parent_reference): bool


plugin trigger types
====================
type match
parent type match
child type match
attribute name from parent match
attribute name of child match
presented length


Plugin templates
================
type presenter
attribute name sorting
alternat formats based on type
alternat formats based on length
alternat formats based on trigger
alternat formats based on options


Default Syntax
==============
attribute     = property-attribute | list-attribute | dict-attribute | sequence-attribute | mapping-attribute
                | simple-native-attribute | complex-navtive-attribute
                | repr-attribute | custom-attribute

property-attribute = property-reference presentation
property-reference = '#' attribute-name
list-attribute = sequence-reference list-presentation
sequence-reference = '[' sequence-index ']'
sequence-index = /\d+/
dict-attribute = mapping-reference dict-presentation
mapping-reference = '[' mapping-key ']'
mapping-key   = presentation-short
sequence-attribute = custom-sequence-attribute | list-attribute
mapping-attribute = custom-mapping-attribute | dict-attribute

presentation  = repr | sequence-repr | mapping-repr | method-repr | initializer_repr
sequence-repr = sequence-repr-short | sequence-repr-long
sequence-repr-short = repr
sequence-repr-long = sequence-repr-list
sequence-repr-list = 'list(' list-length ' itemd)' { list-attribute }
mapping-repr  = mapping-repr-long | mapping-repr-short
method-repr   = '(...)'



Example
=======
Wavefront()
  #file_name= "box-C3F_V3F.obj"
  #mtllibs = list(1 items)
    [0] = Material()
      #name =  "Material"
      #vertex_format = "V3F"
      #vertex_size = 3
      #vertices = list(36 items)
        [0] = [1.0, -1.0, -1.0]
        [1] = [1.0, -1.0, 1.0]
        [2] = [-1.0, -1.0, 1.0]
        . . . . .
        [33] = [-1.0, 1.0, -1.0]
        [34] = [1.0, 1.0, -0.999999]
        [35] = [-1.0, -1.0, -1.0]
      #ambient = [1.0, 1.0, 1.0, 1.0]
      #diffuse = [0.64, 0.64, 0.64, 1.0]
      #emissive = [0.0, 0.0, 0.0, 1.0]
      #gl_floats = None
      #has_colors = False
      #has_normals = False
      #has_uvs = False
      #illumination_model = 2.0
      #is_default = False
      #optical_density = 1.0
      shininess = 96.078431
      specular = [0.5, 0.5, 0.5, 1.0]
      texture(<class 'pywavefront.texture.Texture'>): <pywavefront.texture.Texture object at 0x7fa52a4f59b0>
      texture_alpha = None
      texture_ambient = None
      texture_bump = None
      texture_cls = Texture(3 items)
        [0] = yada yada
        [1] = yada yada
        [2] = yada yada
      texture_specular_color = None
      texture_specular_highlight = None
      transparency = 1.0
      .pad_light(...)
      .set_alpha(...)
      .set_ambient(...)
      .set_diffuse(...)
      .set_emissive(...)
      .set_specular(...)
      .set_texture(...)
      .set_texture_alpha(...)
      .set_texture_ambient(...)
      .set_texture_bump(...)
      .set_texture_specular_color(...)
      .set_texture_specular_highlight(...)
      .unset_texture(...)


      mesh attributes:
        add_material(<class 'method'>): add_material(...)
        faces(<class 'list'>): []
        has_faces(<class 'bool'>): False
        has_material(<class 'method'>): has_material(...)
        materials(<class 'list'>): [<pywavefront.material.Material object at 0x7fa52a4f5908>]
        name(<class 'str'>): 'Cube'
  wavefront attributes:
    add_mesh(<class 'method'>): add_mesh(...)
    file_name(<class 'str'>): '/home/ismael/Projects/render3d/external ... ront/examples/data/box/box-V3F.obj'
    materials(<class 'dict'>): {'Material': <pywavefront.material.Material object at 0x7fa52a4f5908>}
    mesh_list(<class 'list'>): [<pywavefront.mesh.Mesh object at 0x7fa52a4f5860>]
    mtllibs(<class 'list'>): ['box.mtl']
    parse(<class 'method'>): parse(...)
    parser(<class 'pywavefront.obj.ObjParser'>): <pywavefront.obj.ObjParser object at 0x7fa52db0e198>
    parser_cls(<class 'type'>): ObjParser(...)
    vertices(<class 'list'>): [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (- ... -1.0, 1.0, 1.0), (-1.0, 1.0, -1.0)]
