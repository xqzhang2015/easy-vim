# Generated by YCM Generator at 2020-01-06 07:40:39.486254

# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

flags = [
    '-x',
    'c++',
    '-DADS_ENABLE_DEBUG',
    '-DADS_ENABLE_EMBEDDED_LIGHTTPD',
    '-DADS_ENABLE_SELECTOR',
    '-DDEBUG',
    '-DHAVE_CONFIG_H',
    '-DLINUX',
    '-D_GLIBCXX__PTHREADS',
    '-D__STDC_CONSTANT_MACROS',
    '-D__STDC_FORMAT_MACROS',
    '-D__STDC_LIMIT_MACROS',
    '-I.',
    '-I..',
    '-I../3rd',
    '-I../3rd/aws-sdk-cpp/aws-cpp-sdk-core/include',
    '-I../3rd/aws-sdk-cpp/aws-cpp-sdk-s3/include',
    '-I../3rd/curl-7.60.0/include',
    '-I../3rd/sparsehash',
    '-I../3rd/xsdcxx/include',
    '-I../forecast/research/xtr//gen',
    '-I../forecast/research/xtr//include',
    '-I../server/xsd/common',
    '-I../server/xsd/safi-3.0.1',
    '-I../server/xsd/vod-3.0',
    '-I/usr/include/libxml2',
    '-Wall',
    '-Werror',
    '-Wextra',
    '-Wno-deprecated',
    '-Wno-enum-compare',
    '-Wno-missing-field-initializers',
    '-Wno-overloaded-virtual',
    '-Wno-pessimizing-move',
    '-Wno-unneeded-internal-declaration',
    '-Wno-unused',
    '-Wno-unused-function',
    '-Wno-unused-parameter',
    '-Wno-unused-private-field',
    '-Wno-unused-value',
    '-Wno-unused-variable',
    '-Wtype-limits',
    '-std=c++11',
    '-isystem', '../3rd',
    '-isystem', '../3rd/aerospike-common/src/include',
    '-isystem', '../3rd/aerospike-mod-lua/src/include',
    '-isystem', '../3rd/aerospike_client/include',
    '-isystem', '../3rd/etcdv3-cpp/include',
    '-isystem', '../3rd/etcdv3-cpp/proto',
    '-isystem', '../3rd/expat/lib',
    '-isystem', '../3rd/getopt',
    '-isystem', '../3rd/grpc/grpc-1.14.0/include',
    '-isystem', '../3rd/json11',
    '-isystem', '../3rd/kafka/librdkafka/src',
    '-isystem', '../3rd/kafka/librdkafka/src-cpp',
    '-isystem', '../3rd/leveldb/include',
    '-isystem', '../3rd/libevent',
    '-isystem', '../3rd/libevent/include',
    '-isystem', '../3rd/lzma/C',
    '-isystem', '../3rd/protobuf/src',
    '-isystem', '../3rd/snort',
    '-isystem', '/usr/local/include',
]


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.C', '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.H', '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }

def Settings( **kwargs ):
    language = kwargs[ 'language' ]
    if language == 'cfamily':
        return {
            'flags': flags
        }

    return {}